Summary:	MS Windows95/98/NT testing kit
Summary(pl):	Narzêdzie testuj±ce MS Windows-95/98/NT
Name:		targa
Version:	2.1
Release:	4
License:	GPL
Group:		Applications/System
Source0:	%{name}.c
#Source0:	ftp://ftp.ntua.gr/pub/security/technotronic/denial/targa2.c
URL:		http://www.rootshell.com/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	nuks

%description
Package includes Targa -- application that cointains bonk, jolt,
teardrop, newtear, nestea, land, syndrop, winnuke, 1234, saihyousen
and oshare. For educational purposes only, and for MS presentation...

%description -l pl
Pakiet zawiera Targê -- aplikacjê zawieraj±c± podprogramy: bonk, jolt,
teardrop, newtear, nestea, land, syndrop, winnuke, 1234, saiyhousen
oshare.. Pakiet ten jest przeznaczony wy³±cznie do celów edukacyjnych
i do wykorzystania podczas prezentacji przedstawicieli MS...

%prep
%setup -c -T -q
install %{SOURCE0} .

%build
%{__cc} %{rpmcflags} %{rpmldflags} -o targa targa.c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install targa $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/*
