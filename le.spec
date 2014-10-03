Summary:	Terminal text editor LE
Summary(pl.UTF-8):	LE - terminalowy edytor tekstowy
Name:		le
Version:	1.15.0
Release:	1
License:	GPL v2+
Group:		Applications/Editors
Source0:	https://github.com/lavv17/le/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	1b144313fc93f3b08e4f48921ee78541
URL:		https://github.com/lavv17/le
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gnulib
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LE has many block operations with stream and rectangular blocks, can
edit both Unix and DOS style files (LF/CR+LF), is binary clean, has
hex mode, tunable syntax highlighting, tunable color scheme, tunable
key map and some more useful features. It is slightly similar to
Norton Editor from DOS.

%description -l pl.UTF-8
LE potrafi wykonywać wiele operacji blokowych na blokach
strumieniowych i prostokątnych, może modyfikować pliki w formacie Unix
i DOS (LF/CR+LF), nie psuje plików binarnych, ma tryb szesnastkowy,
konfigurowalne podświetlanie składni, konfigurowalne schematy kolorów,
konfigurowalną mapę klawiszy oraz kilka innych przydatnych funkcji.
Jest nieco podobny do Norton Editora dla DOS-a.

%prep
%setup -q

%build
gnulib-tool --update
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
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
%doc BUGS ChangeLog FEATURES HISTORY NEWS README README.md README.regex THANKS TODO
%doc %lang(ru) doc/README.keymap.ru
%attr(755 root root) %{_bindir}/le
%{_mandir}/man1/le.1*
%{_datadir}/%{name}
