# IF asterisk-1.0.6-2 (with h323 enabled by default works)
# this spec is obsoleted,
Summary:	Asterisk PBX - h323 plugin
Summary(pl.UTF-8):	Wtyczka h323 dla centralki Asterisk
Name:		asterisk-oh323
Version:	0.7.1
Release:	0.1
License:	GPL v2
Group:		Applications/System
Source0:	http://www.inaccessnetworks.com/projects/asterisk-oh323/download/%{name}-%{version}.tar.gz
# Source0-md5:	6a78c712e5cfd601aebd4c0fd55cad65
URL:		http://www.inaccessnetworks.com/projects/asterisk-oh323/
BuildRequires:	asterisk-devel
BuildRequires:	openh323-devel
Requires:	asterisk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Asterisk is an Open Source PBX and telephony development platform that
can both replace a conventional PBX and act as a platform for
developing custom telephony applications for delivering dynamic
content over a telephone similarly to how one can deliver dynamic
content through a web browser using CGI and a web server.

Asterisk talks to a variety of telephony hardware including BRI, PRI,
POTS, and IP telephony clients using the Inter-Asterisk eXchange
protocol (e.g. gnophone or miniphone). For more information and a
current list of supported hardware, see http://www.asteriskpbx.com/.

This package contains H323 plugin for Asterisk PBX.

%description -l pl.UTF-8
Asterisk to wolnodostępna centralka (PBX) i platforma programistyczna
dla telefonii, mogąca zastąpić konwencjonalne PBX-y oraz służyć jako
platforma do rozwijania własnych aplikacji telefonicznych do
przekazywania dynamicznej treści przez telefon, podobnie jak można
przekazywać dynamiczną treść przez przeglądarkę WWW przy użyciu CGI i
serwera WWW.

Asterisk współpracuje z wielorakim sprzętem telefonicznym, w tym BRI,
PRI, POTS oraz klienty telefonii IP używające protokołu Inter-Asterisk
eXchange (np. gnophone lub miniphone). Więcej informacji i listę
obsługiwanego sprzętu można znaleźć pod http://www.asteriskpbx.com/.

Ten pakiet zawiera wtyczkę H323 dla centralki Asterisk.

%prep
%setup -q

%build
#wrapper/check_ver /usr/include/pwlib pwlib
#wrapper/check_ver /usr/include/openh323 openh323
#echo "#!/bin/sh" > wrapper/check_ver

%{__make} \
	PWLIBDIR=/usr/include/pwlib \
	OPENH323DIR=/usr/include/openh323 \
	CFLAGS="-Wall %{rpmcflags} -I/usr/include/openh323 -I/usr/include/ptlib -I/usr/include" \
	CPPFLAGS="-Wall %{rpmcflags} -I/usr/include/openh323 -I/usr/include/ptlib -I/usr/X11R6/include \
		-DNDEBUG -DP_LINUX -D_REENTRANT -DP_HAS_SEMAPHORES -DP_SSL \
		-DP_PTHREADS -DPBYTE_ORDER=PLITTLE_ENDIAN -DPHAS_TEMPLATES"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc BUGS ChangeLog CREDITS HARDWARE README* SECURITY configs doc/{*.txt,linkedlists.README}
#%attr(0640,root,root) %config(noreplace) %{_sysconfdir}/asterisk/*.conf
#%attr(0755,root,root) %{_libdir}/asterisk/modules/*.so
