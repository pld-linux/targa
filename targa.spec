Summary:	MS Windows95/98/NT testing kit 
Summary(pl):	Narzêdzie testuj±ce M$ Windows-95/98/NT
Name:		targa
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Version:	2.0
Release:	1
License:	GPL
Source0:	targa.c
URL:		http://www.rootshell.com
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	nuks

%description
Package includes Targa -- application that cointains bonk, jolt, teardrop,
newtear, nestea, land, syndrop, winnuke, 1234, saihyousen and oshare.
For educational purposes only, and for M$ presentation ...

%description -l pl
Pakiet zawiera Targê -- aplikacjê zawieraj±c± podprogramy: bonk, jolt,
teardrop, newtear, nestea, land, syndrop, winnuke, 1234, saiyhousen 
oshare.. Pakiet ten jest przeznaczony wy³±cznie do celów edukacyjnych i do
wykorzystania podczas prezentacji przedstawicieli M$...

%prep
%setup -c -T -q
install %{SOURCE0} $RPM_BUILD_DIR/%{name}-%{version}

%build
cd $RPM_BUILD_DIR/%{name}-%{version}
gcc $RPM_OPT_FLAGS -s -o targa targa.c

%install
rm -rf $RPM_BUILD_ROOT
cd $RPM_BUILD_DIR/%{name}-%{version}

install -d $RPM_BUILD_ROOT%{_sbindir}
install targa $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%attr(755,root,root) %{_sbindir}/*
