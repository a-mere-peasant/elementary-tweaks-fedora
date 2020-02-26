%global commit 5e2e0e1d4ac8da72e616d126a85284902c324224
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20200120

Name:           elementary-tweaks
Summary:        Tweak settings for the Pantheon DE
Version:        0.0.1
Release:        0.%{commitdate}.git%{shortcommit}%{?dist}.1
License:        GPLv3+

URL:            https://github.com/%{name}/%{name}
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite) >= 0.5
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(switchboard-2.0)
BuildRequires:  GConf2-devel


Requires:       hicolor-icon-theme

%description
A tool to easily and safely customize your desktop's appearance.

%prep
%autosetup -n %{name}-%{commit} -p1

%build
%meson
%meson_build


%install
%meson_install
%find_lang %{name}-plug
%files -f %{name}-plug.lang
%doc     README.md
%license COPYING

%{_libdir}/switchboard/personal/libelementary-tweaks.so
%{_datadir}/icons/hicolor/24x24/categories/preferences-tweaks-anim.svg
%{_datadir}/icons/hicolor/24x24/categories/preferences-tweaks-shadows.svg
%{_datadir}/icons/hicolor/32x32/categories/preferences-desktop-tweaks.svg
%{_datadir}/icons/hicolor/32x32/categories/preferences-tweaks-cerbere.svg
%{_datadir}/icons/hicolor/32x32/categories/preferences-tweaks-slingshot.svg

%changelog
* Tue Feb 25 2020 a-mere-peasant - 0.0.1-0.20200120.git5e2e0e1.1
- Initial package for fedora.


