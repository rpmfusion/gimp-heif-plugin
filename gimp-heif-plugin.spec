Name:           gimp-heif-plugin
Version:        1.1.0
Release:        1%{?dist}
Summary:        A plugin for loading and saving HEIF images

License:        GPLv3
URL:            https://github.com/strukturag/heif-gimp-plugin/
Source0:        %{url}/archive/libheif-v%{version}/heif-gimp-plugin-libheif-v%{version}.tar.gz
Patch0:         %{url}/commit/114bb9670b18c76dc9f10a446488c7419a70c7e5.patch#/autogen-1.16.patch

BuildRequires:    autoconf
BuildRequires:    gcc
BuildRequires:    libtool
BuildRequires:    intltool
BuildRequires:    pkgconfig(gimp-2.0)
BuildRequires:    pkgconfig(libheif)

%description
This is a GIMP plugin for loading and saving HEIF images.
HEIF is a image format using HEVC image coding for the best compression ratios.

%prep
%autosetup -p1 -n heif-gimp-plugin-libheif-v%{version}
NOCONFIGURE=1 ./autogen.sh

%build
%configure
%make_build


%install
%make_install
%find_lang gimp20-heif-plugin


%files -f gimp20-heif-plugin.lang
%license COPYING
%doc README.md
%{_libdir}/gimp/2.0/plug-ins/heif-gimp-plugin
%{_datadir}/gimp-heif-plugin/


%changelog
* Fri Nov 30 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.1.0-1
- First build
