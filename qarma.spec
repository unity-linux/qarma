Summary:	A drop-in replacement clone for zenity, written in Qt4/5
Name:		qarma
Version:	1.0
Release:	1%{?dist}
License:	GPLv2
Group:		System/Packaging
URL:		https://github.com/luebking/qarma
Source0:	https://aur.archlinux.org/cgit/aur.git/plain/qarma-1.0.tar.gz?h=qarma
BuildRequires:	gcc
BuildRequires:	qtbase5-common-devel
Requires:	libqt5x11extras5

%description
A drop-in replacement clone for zenity, written in Qt4/5

%prep
%setup -q

%build
qmake -makefile %{name}.pro
qmake
%make

%install
%make_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%license LICENSE
%doc README.md
%{_bindir}/qarma
