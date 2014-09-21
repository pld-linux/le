Summary:	Terminal text editor LE
Name:		le
Version:	1.15.0
Release:	1
License:	GPL
Group:		Applications/Editors
Source0:	https://github.com/lavv17/le/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	1b144313fc93f3b08e4f48921ee78541
URL:		https://github.com/lavv17/le
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LE has many block operations with stream and rectangular blocks, can
edit both unix and dos style files (LF/CRLF), is binary clean, has hex
mode, tunable syntax highlighting, tunable color scheme, tunable key
map and some more useful features. It is slightly similar to Norton
Editor from DOS.

%prep
%setup -q

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc FEATURES HISTORY NEWS README
%doc %lang(ru) doc/README.keymap.ru
%attr(755 root root) %{_bindir}/le
%{_mandir}/man*/*
%{_datadir}/%{name}
