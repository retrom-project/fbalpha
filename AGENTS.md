# Retrom FBAlpha fork

This repository owns the FBAlpha 0.2.97.44 browser core. `master` mirrors
libretro/beetle-finalarcade2019; Retrom integration belongs to
`retrom/gb25b724ba204` and feature branches created from it. Never put Retrom
patches on the upstream mirror or introduce ROM-specific compatibility aliases.

`retrom-fork.json` declares the pinned upstream commit, ABI and closed release
asset set. Build candidates with `.github/rpg-runtime/build-candidate.sh OUTPUT`.
The pinned EmulatorJS RetroArch frontend is fetched to ignored `.cache/`.
DAT must be exported by the exact shipped Wasm; preserve original ROM/BIOS bytes.

Run `python3 -m unittest discover -s .github/rpg-runtime -p 'test_*.py'` and the
native content receipt test in the candidate build. Compare complete archive
hashes from repeated identical builds. Browser integration must verify content
acceptance, standard gamepad input, checkpoint and fresh-instance restoration
through Retrom's public launch flow before merging or releasing.

Do not commit ROMs, BIOS, credentials, caches or built assets. Release tags use
`retrom-core-gb25b724ba204-rN` and are immutable. Publication requires user
approval. The workflow verifies the source, license and complete asset hashes.
