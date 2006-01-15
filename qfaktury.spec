#
# Conditional build:
#%bcond_with	tests		# build with tests
#%bcond_without	tests		# build without tests
#
Summary:	Darmowy i wszechstronny system fakturuj±cy
Name:		qfaktury
Version:	0.0.1
Release:	1
License:	GPL
#Vendor:		-
Group:		Applications
#Icon:		-
Source0:	http://www.e-linux.pl/modules/qfaktury/%{name}-%{version}.tar.gz
# Source0-md5:	f98527d0136dc91391dbd3c2b10b6526
#Source1:	-
# Source1-md5:	-
#Patch0:		%{name}-DESTDIR.patch
URL:		http://www.e-linux.pl/modules/qfaktury/index.php
%if %{with initscript}
BuildRequires:	rpmbuild(macros) >= 1.228
Requires(post,preun):	/sbin/chkconfig
%endif
BuildRequires:	qt-devel >= 3.3
Requires:	qt >= 3.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QFaktury to ca³kowicie darmowy i wszechstronny system fakturuj±cy pracuj±cy
pod kontrol± systemu Linux. Umo¿liwia on drukowanie faktur, faktur pro
forma i korekt, a tak¿e ³atwe zarz±dzanie fakturami, towarami i baza
kontrahentów. Za pomoc± programu QFaktur mo¿liwe jest równie¿ przygotowanie
faktury w formacie PDF czy XML. System integruje siê z programem
e-Przelewy.


%prep
%setup -q -n %{name}

%build
export QTDIR=/usr
qmake
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
install -d $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_bindir}

install -m 755 ./bin/qfaktury $RPM_BUILD_ROOT/%{_bindir}

install -d $RPM_BUILD_ROOT%{_datadir}/qfaktury
install -d $RPM_BUILD_ROOT%{_datadir}/qfaktury/icons

install -c -p -m 644 ./share/qfaktury/icons/dane_firmy.png $RPM_BUILD_ROOT%{_datadir}/qfaktury/icons/dane_firmy.png
install -c -p -m 644 ./share/qfaktury/icons/dodaj_kontrahentow.png $RPM_BUILD_ROOT%{_datadir}/qfaktury/icons/dodaj_kontrahentow.png
install -c -p -m 644 ./share/qfaktury/icons/edytuj_kontrahentow.png $RPM_BUILD_ROOT%{_datadir}/qfaktury/icons/edytuj_kontrahentow.png
install -c -p -m 644 ./share/qfaktury/icons/edytuj_przelew.png $RPM_BUILD_ROOT%{_datadir}/qfaktury/icons/edytuj_przelew.png
install -c -p -m 644 ./share/qfaktury/icons/qfaktury_128.png $RPM_BUILD_ROOT%{_datadir}/qfaktury/icons/qfaktury_128.png
install -c -p -m 644 ./share/qfaktury/icons/qfaktury_16.png $RPM_BUILD_ROOT%{_datadir}/qfaktury/icons/qfaktury_16.png
install -c -p -m 644 ./share/qfaktury/icons/qfaktury_32.png $RPM_BUILD_ROOT%{_datadir}/qfaktury/icons/qfaktury_32.png
install -c -p -m 644 ./share/qfaktury/icons/qfaktury_48.png $RPM_BUILD_ROOT%{_datadir}/qfaktury/icons/qfaktury_48.png
install -c -p -m 644 ./share/qfaktury/icons/qfaktury_64.png $RPM_BUILD_ROOT%{_datadir}/qfaktury/icons/qfaktury_64.png
install -c -p -m 644 ./share/qfaktury/icons/k2.png $RPM_BUILD_ROOT%{_datadir}/qfaktury/icons/k2.png
install -c -p -m 644 ./share/qfaktury/icons/koniec.png $RPM_BUILD_ROOT%{_datadir}/qfaktury/icons/koniec.png
install -c -p -m 644 ./share/qfaktury/icons/kreator.png $RPM_BUILD_ROOT%{_datadir}/qfaktury/icons/kreator.png
install -c -p -m 644 ./share/qfaktury/icons/o_programie.png $RPM_BUILD_ROOT%{_datadir}/qfaktury/icons/o_programie.png
install -c -p -m 644 ./share/qfaktury/icons/splash.png $RPM_BUILD_ROOT%{_datadir}/qfaktury/icons/splash.png
install -c -p -m 644 ./share/qfaktury/icons/ustawienia.png $RPM_BUILD_ROOT%{_datadir}/qfaktury/icons/ustawienia.png
install -c -p -m 644 ./share/qfaktury/icons/usun_kontrahentow.png $RPM_BUILD_ROOT%{_datadir}/qfaktury/icons/usun_kontrahentow.png
install -c -p -m 644 ./share/qfaktury/icons/usun_przelew.png $RPM_BUILD_ROOT%{_datadir}/qfaktury/icons/usun_przelew.png

install -d $RPM_BUILD_ROOT%{_datadir}/qfaktury/templates
install -c -p -m 644 ./share/qfaktury/templates/style.css $RPM_BUILD_ROOT%{_datadir}/qfaktury/templates/style.css

install -d $RPM_BUILD_ROOT%{_desktopdir}
install -c -p  -m 644 ./share/qfaktury/icons/qfaktury.desktop $RPM_BUILD_ROOT%{_desktopdir}/qfaktury.desktop

install -d $RPM_BUILD_ROOT%{_desktopdir}/kde
install -c -p  -m 644 ./share/qfaktury/icons/qfaktury.desktop $RPM_BUILD_ROOT%{_desktopdir}/kde/qfaktury.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%pre

%post

%preun

%postun

%if %{with ldconfig}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%endif

%if %{with initscript}
%post init
/sbin/chkconfig --add %{name}
%service %{name} restart

%preun init
if [ "$1" = "0" ]; then
	%service -q %{name} stop
	/sbin/chkconfig --del %{name}
fi
%endif

%files
%defattr(644,root,root,755)
%doc README TODO FAQ

%attr(755,root,root) %{_bindir}/qfaktury

%{_desktopdir}/kde/qfaktury.desktop
%{_desktopdir}/qfaktury.desktop
%{_datadir}/qfaktury/icons/dane_firmy.png
%{_datadir}/qfaktury/icons/dodaj_kontrahentow.png
%{_datadir}/qfaktury/icons/edytuj_kontrahentow.png
%{_datadir}/qfaktury/icons/edytuj_przelew.png
%{_datadir}/qfaktury/icons/k2.png
%{_datadir}/qfaktury/icons/koniec.png
%{_datadir}/qfaktury/icons/kreator.png
%{_datadir}/qfaktury/icons/o_programie.png
%{_datadir}/qfaktury/icons/qfaktury_128.png
%{_datadir}/qfaktury/icons/qfaktury_16.png
%{_datadir}/qfaktury/icons/qfaktury_32.png
%{_datadir}/qfaktury/icons/qfaktury_48.png
%{_datadir}/qfaktury/icons/qfaktury_64.png
%{_datadir}/qfaktury/icons/splash.png
%{_datadir}/qfaktury/icons/ustawienia.png
%{_datadir}/qfaktury/icons/usun_kontrahentow.png
%{_datadir}/qfaktury/icons/usun_przelew.png
%{_datadir}/qfaktury/templates/style.css

%if 0
# if _sysconfdir != /etc:
#%%dir %{_sysconfdir}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%endif

# initscript and its config
%if %{with initscript}
%attr(754,root,root) /etc/rc.d/init.d/%{name}
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}
%endif

#%{_examplesdir}/%{name}-%{version}
