
%global srcname elementary-tweaks

Name:           elementary-tweaks
Summary:        Eleemntary-tweak tool to customize pantheon desktop
Version:        5.0.3
Release:        1%{?dist}
License:        GPLv3+

Source0:        https://github.com/a-mere-peasant/elementary-tweaks/archive/elementary-tweaks.tar.gz
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  switchboard-devel

Requires:       hicolor-icon-theme


Provides:       elementary-tweaks = %{version}-%{release}


%description
The elementary tweak tool helps to cusomize the pantheon desktop
 enviornment's appearance easily and safely

%prep
%autosetup -n %{srcname} -p1


%build
%meson
%meson_build


%install
%meson_install

%clean
rm -rf %{buildroot}

%files
%doc README.md
%license COPYING
/usr/src/debug/*
/usr/lib64/*
/usr/share/locale/*
/usr/share/icons/hicolor/*
