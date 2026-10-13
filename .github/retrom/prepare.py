from pathlib import Path
import hashlib
import subprocess
import tarfile
import urllib.request
ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / '.cache/retroarch'
COMMIT = '6dd4353937ef48b6ec0bfbdbb15d1c5992d86927'
if not SOURCE.exists():
    subprocess.run(['git','clone','--filter=blob:none','--no-checkout','https://github.com/EmulatorJS/RetroArch',str(SOURCE)],check=True)
    subprocess.run(['git','-C',str(SOURCE),'checkout','--detach',COMMIT],check=True)
if subprocess.check_output(['git','-C',str(SOURCE),'rev-parse','HEAD'],text=True).strip()!=COMMIT:
    raise RuntimeError('RETROARCH_SOURCE_MISMATCH')
subprocess.run(['git','-C',str(SOURCE),'diff','--quiet','HEAD','--'],check=True)

# Archive compression must not depend on the host distro's 7-Zip version.
archive = ROOT / '.cache/7z2501-linux-x64.tar.xz'
expected = '4ca3b7c6f2f67866b92622818b58233dc70367be2f36b498eb0bdeaaa44b53f4'
if not archive.exists():
    with urllib.request.urlopen('https://www.7-zip.org/a/7z2501-linux-x64.tar.xz', timeout=60) as response:
        archive.write_bytes(response.read())
if hashlib.sha256(archive.read_bytes()).hexdigest() != expected:
    raise RuntimeError('PACKAGING_TOOL_SOURCE_MISMATCH')
with tarfile.open(archive, 'r:xz') as package:
    entry = package.getmember('7zz')
    if not entry.isfile():
        raise RuntimeError('PACKAGING_TOOL_INVALID')
    binary = ROOT / '.cache/7zz'
    binary.write_bytes(package.extractfile(entry).read())
    binary.chmod(0o755)
