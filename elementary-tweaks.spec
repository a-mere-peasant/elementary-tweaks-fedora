
Name:           elementary-tweaks
Summary:        Tweak settings for the Pantheon DE
Version:        1.0.1
Release:        1%{?dist}
License:        GPLv3+

URL:            https://github.com/a-mere-peasant/%{name}
Source0:        %{url}/archive/%{name}-%{version}.tar.gz
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite) >= 0.5
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(switchboard-2.0)
BuildRequires:  GConf2-devel


Requires:       hicolor-icon-theme

%description
elementary tweaks is a system panel settings you lets that easily and safely customize your desktop's appearance

%prep
%autosetup -n %{name}-%{version} -p1

%build
%meson
%meson_build


%install
%meson_install

%files
%doc     README.md
%license COPYING

%{_libdir}/switchboard/personal/libelementary-tweaks.so
%{_datadir}/icons/hicolor/*
%{_datadir}/locale/*

%changelog

