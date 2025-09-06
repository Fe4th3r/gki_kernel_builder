from pathlib import Path
from typing import Final, Literal

from kernel_builder.constants import ROOT

# ---- Build Info
KERNEL_NAME: Final[str] = "ZTC"
DEFCONFIG: Final[str] = "gki_defconfig"
BUILD_USER: Final[str] = "gki-builder"
BUILD_HOST: Final[str] = "esk"
IMAGE_COMP: Final[Literal["raw", "lz4", "gz"]] = "gz"

# ---- Kernel
KERNEL_REPO: Final[str] = "github.com:Fe4th3r/android_gki_kernel_5.10_common"
KERNEL_BRANCH: Final[str] = "android12-5.10-2025-06"

# ---- AnyKernel3
ANYKERNEL_REPO = "github.com:ESK-Project/AnyKernel3"
ANYKERNEL_BRANCH = "android12-5.10"

# ---- Release
RELEASE_REPO: Final[str] = "bachnxuan/android12-5.10-lts"
RELEASE_BRANCH: Final[str] = "esk/main"

# ---- Clang
CLANG_VARIANT: Final[Literal["SLIM", "AOSP", "RV", "YUKI", "LILIUM", "NEUTRON"]] = (
    "AOSP"
)

# Optional: Set custom clang link (override CLANG_VARIANT)
CLANG_URL: str | None = None

# ---- Boot Image Config
BOOT_SIGNING_KEY: Final[Path] = ROOT / "key" / "key.pem"
GKI_URL: Final[str] = (
    "https://dl.google.com/android/gki/gki-certified-boot-android12-5.10-2025-05_r1.zip"
)

# ---- Logging
LOGFILE: Final[str | Path | None] = None

if __name__ == "__main__":
    raise SystemExit("This file is meant to be imported, not executed.")
