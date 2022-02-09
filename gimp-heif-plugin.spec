Name:           gimp-heif-plugin
Version:        1.1.0
Release:        11%{?dist}
Summary:        A plugin for loading and saving HEIF images

License:        GPLv3
URL:            https://github.com/strukturag/heif-gimp-plugin/
Source0:        %{url}/archive/libheif-v%{version}/heif-gimp-plugin-libheif-v%{version}.tar.gz

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
autoreconf -fiv
glib-gettextize --copy --force
intltoolize --copy --force --automake

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
* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug 02 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 17 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 04 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 28 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.1.0-6
- Rebuild for new libheif version

* Sun Nov 03 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.1.0-5
- Rebuild for new libheif version

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 03 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.1.0-2
- Don't use autogen script as it is useless

* Fri Nov 30 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.1.0-1
- First build
