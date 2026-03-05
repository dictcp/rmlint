# rmlint fork

implements
- `--match-relative-path` [upstream PR](https://github.com/sahib/rmlint/pull/640) to deduplicate files only with the same relative path

## Usage
```bash
rmlint --progress -KM --match-relative-path /mnt/base // /mnt/portable

# OR via Docker
sudo docker run --rm -it ghcr.io/dictcp/rmlint -T df --progress -KM --match-relative-path /mnt/base // /mnt/portable
# WARN: remember df to avoid baduid in Docker

# OR my preference, adhoc shell in terminal
sudo docker run --rm -it --entrypoint=/bin/bash -v /volume1:/volume1:ro ghcr.io/dictcp/rmlint
# in docker shell:
rmlint -T df --progress -KM --match-relative-path /mnt/base // /mnt/portable
```
