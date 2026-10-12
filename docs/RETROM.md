# FBAlpha 0.2.97.44 browser integration

Upstream: libretro/beetle-finalarcade2019 at
`b25b724ba2046f00f6615a6ffd4eed85a7e367a0`. Its driver sources match Pegasus's
`d584c833cccf3a29b05b527d1dc53c14335fe9b2` build; subsequent upstream changes
only affect build/CI files. This integration exposes arcade ZIP content.

The owned build statically links the complete arcade driver table to the pinned
EmulatorJS RetroArch frontend with Emscripten. The upstream core's ordinary ZIP
name/CRC resolution remains unchanged. Drivers are selected by the mounted ROM
basename; the runtime's shared per-core DAT selection supplies that name.

`retrom_content_load_result` reports the native `retro_load_game` result.
`retrom_export_arcade_dat` exports mandatory requirements from the same shipped
Wasm; optional ROM entries are omitted. The DAT, Wasm archive and provenance
are published together and verified as one asset set. Manual review retains CRC
warnings, and game content and separately required BIOS remain unmodified.

The core supplies libretro serialization. Runtime owns input mapping, whole-file
persistent caching, public checkpoint compression and lifecycle cleanup.

Build: `.github/rpg-runtime/build-candidate.sh /absolute/empty/output`.
Requires Docker, Python 3, a C compiler and Node 24. Compilation is explicit
and uses the pinned SDK image. `.cache/` is local build state. The output archive
has normalized timestamps and file permissions; repeat builds must match its
complete SHA-256. Core and bundled frontend license notices ship in `LICENSE`.
Packaging downloads SHA-256-pinned 7-Zip 25.01 for Linux x64 and fixes the
compression thread count; the host system archive tool is not used.

The browser core reports the upstream version without a checkout-dependent Git
suffix. `GIT_VERSION` is explicitly empty so an ordinary clone and an isolated
worktree produce the same bytes. Exact source identity stays in the candidate
and release descriptors.
