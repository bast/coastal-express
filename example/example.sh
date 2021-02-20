#!/usr/bin/env bash

cx --boundary="$PWD/boundary.txt" \
   --islands="$PWD/islands.txt" \
   --view-angle=90.0 \
   --min-distance=3.0 \
   --max-distance=40.0 \
   --output-dir="$PWD/output"
