Summary:	The SABRE Fighter Plane Simulator.
Name:		sabre
Version:	0.2.3
Release:	6
License:	GPL
Group:		Amusements/Games
Source:		http://sabre.cobite.com/%{name}-%{version}.tar.gz
URL:		http://sabre.cobite.com/
Patch0:		sabre-redhat.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
ExclusiveArch:	%ix86
BuildRequires:	svgalib-devel

%description
SABRE is an on-going game developed for Linux, worked on as a labor of love 
by flight-simulation enthusiasts. At this point, the developers are 
focusing on Korean War-era fighter aircraft, such as the classic North 
American F-86 SabreJet, the F-84 ThunderJet, the F-51 Mustang and the 
Yak-9.  SABRE can run in any svgalib 8 bit color mode, from 320 x 200 to 
1024 x 768. Using a window, higher resolutions can be selected without loss 
of playing speed. See the WHATSNEW document for more details.   

%prep
%setup -q
%patch0 -p1

%build
automake
autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install prefix=$RPM_BUILD_ROOT/usr
install -d $RPM_BUILD_ROOT/usr/lib/sabre
cp -r lib scenarios doc $RPM_BUILD_ROOT/usr/lib/sabre
install -m 755 RunSabre $RPM_BUILD_ROOT/usr/bin
find $RPM_BUILD_ROOT/usr/lib/sabre -name "Makefile*" -exec rm -f {} \;
strip $RPM_BUILD_ROOT/usr/bin/sabre

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc HISTORY README REQUIREMENTS TROUBLE_SHOOTING WHATSNEW
/usr/bin/*
/usr/lib/sabre
