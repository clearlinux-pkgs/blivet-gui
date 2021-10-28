#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : blivet-gui
Version  : 2.3.0.1
Release  : 9
URL      : https://github.com/storaged-project/blivet-gui/releases/download/2.3.0-1/blivet-gui-2.3.0.tar.gz
Source0  : https://github.com/storaged-project/blivet-gui/releases/download/2.3.0-1/blivet-gui-2.3.0.tar.gz
Summary  : Tool for data storages configuration
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: blivet-gui-bin = %{version}-%{release}
Requires: blivet-gui-data = %{version}-%{release}
Requires: blivet-gui-license = %{version}-%{release}
Requires: blivet-gui-man = %{version}-%{release}
Requires: blivet-gui-python = %{version}-%{release}
Requires: blivet-gui-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
[![Copr build status](https://copr.fedorainfracloud.org/coprs/g/storage/blivet-daily/package/blivet-gui/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/g/storage/blivet-daily/package/blivet-gui/)

%package bin
Summary: bin components for the blivet-gui package.
Group: Binaries
Requires: blivet-gui-data = %{version}-%{release}
Requires: blivet-gui-license = %{version}-%{release}

%description bin
bin components for the blivet-gui package.


%package data
Summary: data components for the blivet-gui package.
Group: Data

%description data
data components for the blivet-gui package.


%package license
Summary: license components for the blivet-gui package.
Group: Default

%description license
license components for the blivet-gui package.


%package man
Summary: man components for the blivet-gui package.
Group: Default

%description man
man components for the blivet-gui package.


%package python
Summary: python components for the blivet-gui package.
Group: Default
Requires: blivet-gui-python3 = %{version}-%{release}

%description python
python components for the blivet-gui package.


%package python3
Summary: python3 components for the blivet-gui package.
Group: Default
Requires: python3-core

%description python3
python3 components for the blivet-gui package.


%prep
%setup -q -n blivet-gui-2.3.0
cd %{_builddir}/blivet-gui-2.3.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1628538080
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/blivet-gui
cp %{_builddir}/blivet-gui-2.3.0/COPYING %{buildroot}/usr/share/package-licenses/blivet-gui/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/blivet-gui-2.3.0/translation-canary/COPYING %{buildroot}/usr/share/package-licenses/blivet-gui/01a6b4bf79aca9b556822601186afab86e8c4fbf
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/blivet-gui
/usr/bin/blivet-gui-daemon

%files data
%defattr(-,root,root,-)
/usr/share/appdata/blivet-gui.appdata.xml
/usr/share/applications/blivet-gui.desktop
/usr/share/blivet-gui/css/rectangle.css
/usr/share/blivet-gui/img/line.png
/usr/share/blivet-gui/ui/about_dialog.ui
/usr/share/blivet-gui/ui/add_disklabel_dialog.ui
/usr/share/blivet-gui/ui/blivet-gui.ui
/usr/share/blivet-gui/ui/cache_area.ui
/usr/share/blivet-gui/ui/confirm_actions_dialog.ui
/usr/share/blivet-gui/ui/confirm_delete_dialog.ui
/usr/share/blivet-gui/ui/confirm_dialog.ui
/usr/share/blivet-gui/ui/custom_dialog.ui
/usr/share/blivet-gui/ui/encryption_chooser.ui
/usr/share/blivet-gui/ui/error_dialog.ui
/usr/share/blivet-gui/ui/exception_dialog.ui
/usr/share/blivet-gui/ui/format_dialog.ui
/usr/share/blivet-gui/ui/info_dialog.ui
/usr/share/blivet-gui/ui/label_dialog.ui
/usr/share/blivet-gui/ui/luks_passphrase_dialog.ui
/usr/share/blivet-gui/ui/mountpoint_dialog.ui
/usr/share/blivet-gui/ui/parent_area.ui
/usr/share/blivet-gui/ui/parent_chooser.ui
/usr/share/blivet-gui/ui/raid_chooser.ui
/usr/share/blivet-gui/ui/resize_dialog.ui
/usr/share/blivet-gui/ui/root_check_window.ui
/usr/share/blivet-gui/ui/show_actions_dialog.ui
/usr/share/blivet-gui/ui/size_area.ui
/usr/share/blivet-gui/ui/size_chooser.ui
/usr/share/blivet-gui/ui/unmount_dialog.ui
/usr/share/blivet-gui/ui/warning_dialog.ui
/usr/share/icons/hicolor/16x16/apps/blivet-gui.png
/usr/share/icons/hicolor/22x22/apps/blivet-gui.png
/usr/share/icons/hicolor/24x24/apps/blivet-gui.png
/usr/share/icons/hicolor/256x256/apps/blivet-gui.png
/usr/share/icons/hicolor/32x32/apps/blivet-gui.png
/usr/share/icons/hicolor/48x48/apps/blivet-gui.png
/usr/share/icons/hicolor/64x64/apps/blivet-gui.png
/usr/share/polkit-1/actions/org.fedoraproject.pkexec.blivet-gui.policy

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/blivet-gui/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/blivet-gui/4cc77b90af91e615a64ae04893fdffa7939db84c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/blivet-gui.1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
