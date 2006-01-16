Summary:	Free software for creating, managing, and printing invoices
Summary(pl):	Darmowy i wszechstronny system fakturuj±cy
Name:		qfaktury
Version:	0.0.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.e-linux.pl/modules/qfaktury/%{name}-%{version}.tar.gz
# Source0-md5:	f98527d0136dc91391dbd3c2b10b6526
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
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
install -d $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_datadir}/{kde,qfaktury/{icons,templates}}
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

install bin/qfaktury $RPM_BUILD_ROOT%{_bindir}

install share/qfaktury/icons/dane_firmy.png $RPM_BUILD_ROOT%{_datadir}/qfaktury/icons/dane_firmy.png
install share/qfaktury/icons/dodaj_kontrahentow.png $RPM_BUILD_ROOT%{_datadir}/qfaktury/icons/dodaj_kontrahentow.png
install share/qfaktury/icons/edytuj_kontrahentow.png $RPM_BUILD_ROOT%{_datadir}/qfaktury/icons/edytuj_kontrahentow.png
install share/qfaktury/icons/edytuj_przelew.png $RPM_BUILD_ROOT%{_datadir}/qfaktury/icons/edytuj_przelew.png
install share/qfaktury/icons/qfaktury_128.png $RPM_BUILD_ROOT%{_datadir}/qfaktury/icons/qfaktury_128.png
install share/qfaktury/icons/qfaktury_16.png $RPM_BUILD_ROOT%{_datadir}/qfaktury/icons/qfaktury_16.png
install share/qfaktury/icons/qfaktury_32.png $RPM_BUILD_ROOT%{_datadir}/qfaktury/icons/qfaktury_32.png
install share/qfaktury/icons/qfaktury_48.png $RPM_BUILD_ROOT%{_datadir}/qfaktury/icons/qfaktury_48.png
install share/qfaktury/icons/qfaktury_64.png $RPM_BUILD_ROOT%{_datadir}/qfaktury/icons/qfaktury_64.png
install share/qfaktury/icons/k2.png $RPM_BUILD_ROOT%{_datadir}/qfaktury/icons/k2.png
install share/qfaktury/icons/koniec.png $RPM_BUILD_ROOT%{_datadir}/qfaktury/icons/koniec.png
install share/qfaktury/icons/kreator.png $RPM_BUILD_ROOT%{_datadir}/qfaktury/icons/kreator.png
install share/qfaktury/icons/o_programie.png $RPM_BUILD_ROOT%{_datadir}/qfaktury/icons/o_programie.png
install share/qfaktury/icons/splash.png $RPM_BUILD_ROOT%{_datadir}/qfaktury/icons/splash.png
install share/qfaktury/icons/ustawienia.png $RPM_BUILD_ROOT%{_datadir}/qfaktury/icons/ustawienia.png
install share/qfaktury/icons/usun_kontrahentow.png $RPM_BUILD_ROOT%{_datadir}/qfaktury/icons/usun_kontrahentow.png
install share/qfaktury/icons/usun_przelew.png $RPM_BUILD_ROOT%{_datadir}/qfaktury/icons/usun_przelew.png

install share/qfaktury/templates/style.css $RPM_BUILD_ROOT%{_datadir}/qfaktury/templates/style.css

install share/qfaktury/icons/qfaktury.desktop $RPM_BUILD_ROOT%{_desktopdir}/qfaktury.desktop
install share/qfaktury/icons/qfaktury_48.png $RPM_BUILD_ROOT%{_pixmapsdir}/qfaktury.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO FAQ
%attr(755,root,root) %{_bindir}/qfaktury
%{_datadir}/qfaktury
%{_desktopdir}/qfaktury.desktop
%{_pixmapsdir}/qfaktury.png
