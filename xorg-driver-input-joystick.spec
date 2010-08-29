Summary:	X.org input driver for joysticks
Summary(pl.UTF-8):	Sterownik wejściowy X.org dla joysticków
Name:		xorg-driver-input-joystick
Version:	1.5.0
Release:	2
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-input-joystick-%{version}.tar.bz2
# Source0-md5:	79b20f86d1b2e625ae65e35c3457027f
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-inputproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-util-util-macros >= 1.2
BuildRequires:	xorg-xserver-server-devel >= 1.3.99.901
BuildRequires:	rpmbuild(macros) >= 1.389
%{?requires_xorg_xserver_xinput}
Requires:	xorg-xserver-server >= 1.3.99.901
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org input driver for joysticks.

%description -l pl.UTF-8
Sterownik wejściowy X.org dla joysticków.

%package devel
Summary:	X.org joystick input driver - properties definition
Summary(pl.UTF-8):	Sterownik wejściowy X.org dla joysticków - definicje właściwości
Group:		Development/Libraries
# for dir
Requires:	xorg-xserver-server-devel
# doesn't require base

%description devel
X.org joystick input driver - properties definition.

%description devel -l pl.UTF-8
Sterownik wejściowy X.org dla joysticków - definicje właściwości.

%prep
%setup -q -n xf86-input-joystick-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/xorg/modules/input/joystick_drv.so
%{_mandir}/man4/joystick.4*

%files devel
%defattr(644,root,root,755)
%{_includedir}/xorg/joystick-properties.h
%{_pkgconfigdir}/xorg-joystick.pc
