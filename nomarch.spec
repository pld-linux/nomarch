Summary:	nomarch - extract ".arc" files
Summary(pl.UTF-8):   nomarch - rozpakowywanie plików .arc
Name:		nomarch
Version:	1.4
Release:	1
License:	GPL v2+
Group:		Applications/Archiving
Source0:	ftp://ftp.ibiblio.org/pub/Linux/utils/compress/%{name}-%{version}.tar.gz
# Source0-md5:	1b0be450e2af64710f9627f85d1b0130
URL:		http://rus.members.beeb.net/nomarch.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
nomarch extracts files from the old `.arc' archive format. It can also
list and test such archives.

It's primarily intended as a `replacement' for the non-Free `arc'
program.

%description -l pl.UTF-8
nomarch rozpakowuje pliki z archiwów w starym formacie .arc. Może
także pokazywać zawartość i testować takie archiwa. Jest pomyślany
głównie jako zamiennik dla programu arc, który ma bardziej
restrykcyjną licencję.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/nomarch
%{_mandir}/man1/nomarch.1*
