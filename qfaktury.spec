
%define		_pre		_pre2

Summary:	Free software for creating, managing, and printing invoices
Summary(pl):	Darmowy i wszechstronny system fakturuj±cy
Name:		qfaktury
Version:	0.0.2
Release:	0.%{_pre}.2
License:	GPL
Group:		X11/Applications
Source0:	http://www.e-linux.pl/modules/qfaktury/%{name}-%{version}%{_pre}.tar.gz
# Source0-md5:	e4a8b18d4a926053c8fb8689ddfcbda5
Patch0:		%{name}-desktop.patch
URL:		http://www.e-linux.pl/modules/qfaktury/index.php
BuildRequires:	qmake
BuildRequires:	qt-devel >= 3.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QFaktury is a software for creating, managing, and printing invoices.
It also maintains a database for contractor information, and a
database for product information. QFaktury was created for a Polish
financial system, but it can be useful in other countries with or
without small modifications.

%description -l pl
QFaktury to ca³kowicie darmowy i wszechstronny system fakturuj±cy
pracuj±cy pod kontrol± systemu Linux. Umo¿liwia on drukowanie faktur,
faktur pro forma i korekt, a tak¿e ³atwe zarz±dzanie fakturami,
towarami i baza kontrahentów. Za pomoc± programu QFaktur mo¿liwe jest
równie¿ przygotowanie faktury w formacie PDF czy XML. System integruje
siê z programem e-Przelewy.


%prep
%setup -q -n %{name}
%patch -p1

%build
export QTDIR=/usr
qmake
%{__make} QTDIR=/usr

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary

rm -f install install.sh

install -d $RPM_BUILD_ROOT%{_pixmapsdir}
install share/qfaktury/icons/qfaktury_48.png $RPM_BUILD_ROOT%{_pixmapsdir}/qfaktury.png

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT \
	QTDIR=/usr


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO FAQ
%attr(755,root,root) %{_bindir}/qfaktury
%{_datadir}/qfaktury
%{_desktopdir}/qfaktury.desktop
%{_pixmapsdir}/qfaktury.png
