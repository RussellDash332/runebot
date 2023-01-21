# Rune Compiler Bot

![Version](https://img.shields.io/badge/version-3.0.1-blue)

This Telegram bot simply compiles your runes, specifically CS1010S runes! Play with functional abstraction and understand why.

An (outdated) demonstration video might help you understand how the bot works.

[Outdated Demo Video](https://user-images.githubusercontent.com/63991775/132953515-80f6453a-c5c8-46a8-b2ed-22c458e08490.mp4)

## Building

1. Create a Telegram bot using BotFather. Note down the provided bot API token.
1. Rename `env.py.example` to `env.py` and paste the token accordingly.
1. Run the following command on Docker to build the Docker image.

    ```
    docker build -t runebot .
    ```
1. Finally run a Docker container using the built image.

    ```
    docker run --name <container_name> -d runebot
    ```

    You may rename `<container_name>` as you wish.