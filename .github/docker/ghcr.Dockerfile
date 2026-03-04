FROM debian:bookworm AS builder

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    clang \
    gettext \
    libblkid-dev \
    libelf-dev \
    libffi-dev \
    libglib2.0-dev \
    libjson-glib-dev \
    python3-cffi \
    python3-dev \
    python3-pip \
    python3-setuptools \
    python3-sphinx \
    scons \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /src
COPY . .

RUN scons config \
  && scons VERBOSE=0 DEBUG=0 O=release \
  && scons --prefix=/usr O=release install

FROM debian:bookworm-slim

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    libblkid1 \
    libelf1 \
    libglib2.0-0 \
    libjson-glib-1.0-0 \
  && rm -rf /var/lib/apt/lists/*

COPY --from=builder /usr/bin/rmlint /usr/local/bin/rmlint

ENTRYPOINT ["/usr/local/bin/rmlint"]
