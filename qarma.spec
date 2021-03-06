%define debug_package %{nil}

Summary:	A drop-in replacement clone for zenity, written in Qt4/5
Name:		qarma
Version:	1.0
Release:	4%{?dist}
License:	GPLv2
Group:		System/Packaging
URL:		https://github.com/luebking/qarma
Source0:	https://aur.archlinux.org/cgit/aur.git/plain/qarma-1.0.tar.gz?h=qarma
BuildRequires:	gcc
BuildRequires:	qtbase5-common-devel
BuildRequires:	pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Widgets)

%description
A drop-in replacement clone for zenity, written in Qt4/5

%prep
%setup -q

%build
qmake -makefile %{name}.pro
qmake
%make

%install
mkdir -p $RPM_BUILD_ROOT/usr/bin/
install qarma $RPM_BUILD_ROOT/usr/bin/
strip $RPM_BUILD_ROOT/usr/bin/qarma

%clean
rm -rf $RPM_BUILD_ROOT

%files
%license LICENSE
%doc README.md
%{_bindir}/qarma

%changelog
* Wed Apr 11 2018 Jeremiah Summers <jsummers@glynlyon.com> 1.0-4
- Add Qt5Core

* Wed Apr 11 2018 Jeremiah Summers <jsummers@glynlyon.com> 1.0-3
- Add X11 Entras as BuildRequires
* Wed Apr 11 2018 Jeremiah Summers <jsummers@glynlyon.com> 1.0-2
- Add Travis files (jsummers@glynlyon.com)
- Fix requires to use pkgconfig
