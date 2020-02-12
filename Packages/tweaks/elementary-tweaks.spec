
%global srcname elementary-tweaks

Name:           elementary-tweaks
Summary:        Eleemntary-tweak tool to customize pantheon desktop
Version:        5.0.3
Release:        1%{?dist}
License:        GPLv3+

Source0:        https://sourceforge.net/projects/elementary-tweaks/files/elementary-tweaks.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  switchboard-devel

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite) >= 0.5
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(switchboard-2.0)
BuildRequires:  GConf2-devel


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

%{_libdir}
%{_datadir}
