Summary: The SABRE Fighter Plane Simulator.
Name: sabre
%define version %{version}
Version: 0.2.3
Release: 5
Copyright: GPL
Group: Amusements/Games
Source: http://sabre.cobite.com/sabre-0.2.3.tar.gz
Url: http://sabre.cobite.com
Patch0: sabre-0.2.3-redhat.patch
BuildRoot: /var/tmp/sabre-root
ExclusiveArch: i386
Requires: svgalib

%description
SABRE is an on-going game developed for Linux, worked on as a labor of
love by flight-simulation enthusiasts.  At this point, the developers
are focusing on Korean War-era fighter aircraft, such as the classic
North American F-86 SabreJet, the F-84 ThunderJet, the F-51 Mustang
and the Yak-9.  SABRE can run in any svgalib 8 bit color mode, from
320 x 200 to 1024 x 768. Using a window, higher resolutions can be
selected without loss of playing speed. See the WHATSNEW document for
more details.

%prep
%setup -q
%patch0 -p1 -b .redhat

%build
automake
autoconf
CC=egcs CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr
make CC=egcs

%install
rm -rf $RPM_BUILD_ROOT
make install prefix=$RPM_BUILD_ROOT/usr
mkdir -p $RPM_BUILD_ROOT/usr/lib/sabre
cp -r lib scenarios doc $RPM_BUILD_ROOT/usr/lib/sabre
install -m 755 RunSabre $RPM_BUILD_ROOT/usr/bin
find $RPM_BUILD_ROOT/usr/lib/sabre -name "Makefile*" -exec rm -f {} \;
strip $RPM_BUILD_ROOT/usr/bin/sabre

%files
%defattr(-,root,root)
%doc HISTORY INSTALL README REQUIREMENTS TROUBLE_SHOOTING WHATSNEW
/usr/bin/*
/usr/lib/sabre

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Jul 21 1999 Tim Powers <timp@redhat.com>
- rebuilt for 6.1

* Thu Apr 15 1999 Michael Maher <mike@redhat.com>
- built package after munging it from falling asleep at my keyboard
  which resulted in lots of extra characters being placed in this file.

* Fri Oct 08 1998 Michael Maher <mike@redhat.com>
- built package for 5.2 powertools

* Fri May 22 1998 Cristian Gafton <gafton@redhat.com>
- packages for PowerTools
