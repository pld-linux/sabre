Summary:	The SABRE Fighter Plane Simulator
Summary(pl):	SABRE - symulator my¶liwca
Name:		sabre
Version:	0.2.3
Release:	6
License:	GPL
Group:		Applications/Games
Source0:	http://sabre.cobite.com/%{name}-%{version}.tar.gz
URL:		http://sabre.cobite.com/
Patch0:		%{name}-redhat.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
ExclusiveArch:	%{ix86}
BuildRequires:	svgalib-devel
BuildRequires:	autoconf
BuildRequires:	automake

%description
SABRE is an on-going game developed for Linux, worked on as a labor of
love by flight-simulation enthusiasts. At this point, the developers
are focusing on Korean War-era fighter aircraft, such as the classic
North American F-86 SabreJet, the F-84 ThunderJet, the F-51 Mustang
and the Yak-9. SABRE can run in any svgalib 8 bit color mode, from 320
x 200 to 1024 x 768. Using a window, higher resolutions can be
selected without loss of playing speed. See the WHATSNEW document for
more details.

%description -l pl
SABRE jest gr± pod Linuksa dla entuzjastów symulacji lotu. W tej
chwili programi¶ci skupili siê na lotnictwie wojennym z czasów wojny w
Korei, takich jak klasyczne pó³nocnoamerykañskie F-86 SabreJet, F-84
ThunderJet, F-51 Mustang i Yak-9. SABRE mo¿e dzia³aæ w trybach
8-bitowych svgalib, od 320x200 do 1024x768.

%prep
%setup -q
%patch0 -p1

%build
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install prefix=$RPM_BUILD_ROOT%{_prefix}
install -d $RPM_BUILD_ROOT%{_libdir}/sabre
cp -r lib scenarios doc $RPM_BUILD_ROOT%{_libdir}/sabre
install -m 755 RunSabre $RPM_BUILD_ROOT%{_bindir}
find $RPM_BUILD_ROOT%{_libdir}/sabre -name "Makefile*" -exec rm -f {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc HISTORY README REQUIREMENTS TROUBLE_SHOOTING WHATSNEW
%attr(755,root,root) %{_bindir}/*
%{_libdir}/sabre
