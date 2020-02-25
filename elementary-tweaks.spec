%global commit 5e2e0e1d4ac8da72e616d126a85284902c324224
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20200120

Name:           elementary-tweaks
Summary:        Tweak settings for the Pantheon DE
Version:        0.0.1
Release:        1.%{commitdate}.git%{shortcommit}%{?dist}
License:        GPLv3+

URL:            https://github.com/%{name}/%{name}
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
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
%autosetup -n %{name}-%{commit} -p1

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

