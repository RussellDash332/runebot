def flatten_once(ls):
	return [element for tupl in ls for element in tupl]

import math
from math import *

visible = None
viewport_size = None;
image_buffer = None
img_antialias = 1

try:
	from PIL import Image, ImageDraw, ImageTk # Import DNSPython
	PIL_available = True
except ImportError:
	PIL_available = False
	print("Warning: PIL was not loaded correctly")

def init(vp_size):
	global viewport_size
	viewport_size = vp_size
	return

# Graphics Auxiliary
class Posn:
	def __init__(self, x = None, y = None):
		if x is None:
			raise TypeError("Posn(x,y) - x must be a number")
		if y is None:
			raise TypeError("Posn(x,y) - y must be a number")
		self.x = x
		self.y = y
	def __add__(self, other):
		return Posn(self.x+other.x, self.y+other.y)
	def __mul__(self, factor):
		return Posn(self.x*factor, self.y*factor)

def open_pixmap(name, horiz, vert):
	global viewport_size, PIL_available
	image = None
	if PIL_available:
		image = Image.new("RGB", (int(horiz), int(vert)), "white")
	return [None, image] # originally [vp, image]

def clear_viewport(viewport):
	if PIL_available:
		size = viewport[1].size # (width, height)
		viewport[1].paste("white", (0,0,size[0], size[1]))

## Drawing capabilities

def draw_line(viewport, p1, p2, color):
	if PIL_available:
		draw = ImageDraw.Draw(viewport[1])
		draw.line(p1.x, p1.y, p2.x, p2.y, fill=color.hexcode())

#poly =  canvas.create_polygon(x0, y0, x1, y1, ..., option, ...)
#points is a list of point objects, need to map and unpack interior twice.
def draw_solid_polygon(viewport, points, offset, color):
	points = flatten_once(map(lambda q: (q.x+offset.x, q.y+offset.y), points))
	#print(*points)
	if PIL_available:
		draw = ImageDraw.Draw(viewport[1])
		draw.polygon(points, fill=color.hexcode())

class Rgb:
	def __init__(self, r,g,b):
		self.r = round(r*255)
		self.g = round(g*255)
		self.b = round(b*255)
	def hexcode(self):
		return '#%02x%02x%02x' % (self.r, self.g, self.b)

import datetime
def saveImage(vp, filename=None):
	if PIL_available:
		if(filename == None):
			filename = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
		vp[1].save(filename+".png", "PNG")
	else:
		print("PIL does not appear to be available")

def get_pixels(vp):
	if PIL_available:
		return vp[1].load()
	else:
		raise("PIL does not appear to be available")

def get_image(vp):
	return vp[1]

def square(x):
	return x*x

def distance(p1, p2):
	return sqrt(square(p1.x-p2.x)+square(p1.y-p2.y))

def blit_pixels(viewport, inv_transform, pixels, viewport_size, image_size, mono, zmin = 0, zmax = 1):
	MAX_X = viewport_size[0]
	MAX_Y = viewport_size[1]
	IMAX_X = image_size[0]
	IMAX_Y = image_size[1]
	viewport_pix = get_pixels(viewport)
	for y in range(MAX_Y):
		for x in range(MAX_X):
			src = inv_transform(Posn(x,y))
			srcx = src.x
			srcy = src.y
			rsrcx = round(srcx)
			rsrcy = round(srcy)
			if(rsrcx>=0 and rsrcx<IMAX_X and rsrcy>=0 and rsrcy<IMAX_Y):
				dsrcx = srcx - rsrcx #+ve => right
				dsrcy = srcy - rsrcy #+ve => up
				if(dsrcx>=0):
					esrcx = 1
				else:
					esrcx = -1
				if(dsrcy>=0):
					esrcy = 1
				else:
					esrcy = -1
				original = Posn(srcx, srcy)
				dtgt = 1/(distance(Posn(rsrcx, rsrcy),original)+0.01)
				dtgtdx = 1/(distance(Posn(rsrcx+esrcx, rsrcy),original)+0.01)
				dtgtdy = 1/(distance(Posn(rsrcx, rsrcy+esrcy),original)+0.01)
				dtgtdxdy = 1/(distance(Posn(rsrcx+esrcx, rsrcy+esrcy),original)+0.01)
				tgt = pixels[rsrcx, rsrcy]
				if(rsrcx+esrcx>= 0 and rsrcx+esrcx<IMAX_X):
					tgtdx = pixels[rsrcx+esrcx, rsrcy]
				else:
					dtgtdx = 0
					dtgtdxdy = 0
					tgtdx = (0,0,0)
				if(rsrcy+esrcy>= 0 and rsrcy+esrcy<IMAX_Y):
					tgtdy = pixels[rsrcx, rsrcy+esrcy]
				else:
					dtgtdy = 0
					dtgtdxdy = 0
					tgtdy = (0,0,0)
				if(dtgtdxdy!=0):
					tgtdxdy = pixels[rsrcx+esrcx, rsrcy+esrcy]
				else:
					tgtdxdy = (0,0,0)
				divisor = (dtgt + dtgtdx + dtgtdy + dtgtdxdy)
				tcolor = (round((dtgt*tgt[0]+dtgtdx*tgtdx[0]+dtgtdy*tgtdy[0]+dtgtdxdy*tgtdxdy[0])/divisor),\
				round((dtgt*tgt[1]+dtgtdx*tgtdx[1]+dtgtdy*tgtdy[1]+dtgtdxdy*tgtdxdy[1])/divisor), \
				round((dtgt*tgt[2]+dtgtdx*tgtdx[2]+dtgtdy*tgtdy[2]+dtgtdxdy*tgtdxdy[2])/divisor))
				def rescale(color):
					if color>=254:
						return 255
					else:
						return round(zmin*255 + (zmax-zmin)*color)
				tcolor = (rescale(tcolor[0]), rescale(tcolor[1]), rescale(tcolor[2]))
				viewport_pix[x,y] = (min(tcolor[0], viewport_pix[x,y][0]), min(tcolor[1], viewport_pix[x,y][1]), min(tcolor[2], viewport_pix[x,y][2]))

def get_image_size(img):
	return img[1].size

def load_image(filename): #returns a vp
	global img_antialias
	if PIL_available:
		img = Image.open(filename)
		img = img.convert('RGB')
		width, height = img.size
		img = img.resize((img_antialias*width, img_antialias*height), Image.BICUBIC)
		return (None, img)
	else:
		raise("load_img requires that PIL be available")
