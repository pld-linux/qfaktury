Summary:	Free software for creating, managing, and printing invoices
Summary(pl.UTF-8):	Darmowy i wszechstronny system fakturujący
Name:		qfaktury
Version:	0.6.2
Release:	1
License:	GPL v3
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/sourceforge/qfaktury/%{name}-%{version}.tar.gz
# Source0-md5:	047f8239bf6187c9da9b69f90f284c15
Patch0:		%{name}-desktop.patch
Patch1:		build.patch
URL:		http://qfaktury.sourceforge.net/
BuildRequires:	qt4-build
BuildRequires:	qt4-qmake
BuildRequires:	Qt3Support-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QFaktury is a software for creating, managing, and printing invoices.
It also maintains a database for contractor information, and a
database for product information. QFaktury was created for a Polish
financial system, but it can be useful in other countries with or
without small modifications.

%description -l pl.UTF-8
QFaktury to całkowicie darmowy i wszechstronny system fakturujący
pracujący pod kontrolą systemu Linux. Umożliwia on drukowanie faktur,
faktur pro forma i korekt, a także łatwe zarządzanie fakturami,
towarami i baza kontrahentów. Za pomocą programu QFaktury możliwe jest
również przygotowanie faktury w formacie PDF czy XML. System integruje
się z programem e-Przelewy.

%prep
%setup -q 
#%patch0 -p1
%patch1 -p1
sed -i -e 's|/usr/lib/qt4/mkspecs|/usr/share/qt4/mkspecs|g' Makefile

%build
%{__make} \
	QMAKE=/usr/bin/qmake-qt4 \
	CXXFLAGS="%{rpmcxxflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ReadMe.txt
%attr(755,root,root) %{_bindir}/qfaktury
%{_datadir}/qfaktury
%{_desktopdir}/QFaktury.desktop
