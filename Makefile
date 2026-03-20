# Arch Parental Controls Makefile

.PHONY: all clean build-rust build-python package install-deps test

VERSION := $(shell grep "^pkgver=" pkgbuild/PKGBUILD | cut -d= -f2)

all: build-rust build-python package

# 1. Build the Rust D-Bus Daemon
build-rust:
	cd age-signal && cargo build --release

# 2. Build the Python Package (Wheel)
build-python:
	python -m build --wheel --no-isolation

# 3. Create the Arch Linux Package (.pkg.tar.zst)
package:
	@echo "Creating source tarball for v$(VERSION)..."
	rm -rf pkgbuild/pkg pkgbuild/src pkgbuild/dist pkgbuild/*.pkg.tar.zst
	tar -czf pkgbuild/arch-parental-controls-$(VERSION).tar.gz --exclude=pkgbuild --exclude=.git --exclude=.pytest_cache .
	cd pkgbuild && makepkg -Cf --noconfirm --nodeps

# 4. Install Dependencies (Arch Linux)
install-deps:
	sudo pacman -S --needed python-gobject gtk4 libadwaita polkit nftables systemd acl cargo python-build python-installer python-setuptools python-wheel gettext

# 5. Run Tests
test:
	pytest tests

# 6. Clean Build Artifacts
clean:
	rm -rf dist/
	rm -rf age-signal/target/
	rm -rf pkgbuild/pkg/ pkgbuild/src/ pkgbuild/*.pkg.tar.zst pkgbuild/*.tar.gz
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
