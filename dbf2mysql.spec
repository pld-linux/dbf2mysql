Summary:	Tool for creating converters from dbf files to MySQL commands
Summary(pl.UTF-8):   Narzędzie do tworzenia konwerterów plików dbf na instrukcje MySQL
Name:		dbf2mysql
Version:	1.14a
Release:	1
License:	GPL
Group:		Applications/Databases
Source0:	ftp://ftp.debian.org/debian/pool/main/d/dbf2mysql/%{name}_%{version}.orig.tar.gz
# Source0-md5:	381f69bf6aa5d8dbed8a4ac129d63a6c
Patch0:		%{name}-debian.patch
URL:		http://dbf2mysql.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dbf2mysql is a little tool that will display dBase III and IV files.
You can also use it to convert your old .dbf files for further use
with MySQL.

%description -l pl.UTF-8
dbf2mysql jest małym programem wyświetlającym zawartość plików dBase
III i IV. Można go wykorzystać do konwersji starych plików .dbf do
wykorzystania pod MySQL.

%prep
%setup -q
%patch0 -p1
patch -p1 < debian/patches/mysql.dpatch || exit 1
patch -p1 < debian/patches/05_mysql_real_connect.dpatch || exit 1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	MYSQLLIB="-L%{_libdir}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install dbf2mysql mysql2dbf $RPM_BUILD_ROOT%{_bindir}
install debian/dbf2mysql.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
