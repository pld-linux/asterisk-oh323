Summary:	Asterisk PBX - h323 plugin
Name:		asterisk-oh323
Version:	0.2
Release:	0.1
License:	GPL v2
Group:		Applications/System
Source0:	ftp://ftp.asterisk.org/pub/telephony/asterisk/h323/%{name}-%{version}.tar.gz
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
current list of supported hardware, see www.asteriskpbx.com.

%prep
%setup -q -n %{name}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	INSTALL_PREFIX=$RPM_BUILD_ROOT
%files
%defattr(644,root,root,755)
#%doc BUGS ChangeLog CREDITS HARDWARE README* SECURITY configs doc/{*.txt,linkedlists.README}
#%attr(0640,root,root) %config(noreplace) %{_sysconfdir}/asterisk/*.conf
#%attr(0755,root,root) %{_libdir}/asterisk/modules/*.so

%clean
rm -rf $RPM_BUILD_ROOT
