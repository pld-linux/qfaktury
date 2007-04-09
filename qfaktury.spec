
%define		_pre		rc1
%define		qversion	0_1a
Summary:	Free software for creating, managing, and printing invoices
Summary(pl.UTF-8):	Darmowy i wszechstronny system fakturujący
Name:		qfaktury
Version:	0.1a
Release:	1.%{_pre}.3
License:	GPL
Group:		X11/Applications
Source0:	http://www.e-linux.pl/download/task,doc_download/gid,15/%{name}
# Source0-md5:	13fed849ec20c66cab5e22aa6f9e783e
Patch0:		%{name}-desktop.patch
URL:		http://www.e-linux.pl
BuildRequires:	qmake
BuildRequires:	qt-devel >= 6:3.3
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
%setup -q -n %{name}
%patch0 -p1

# remove CVS control files
find -name cvs -print0 | xargs -0 rm -rf

%build
export QTDIR=/usr
./configure 
qmake
%{__make} QTDIR=/usr

%install
rm -rf $RPM_BUILD_ROOT

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
%doc readme todo faq
%attr(755,root,root) %{_bindir}/qfaktury
%{_datadir}/qfaktury
%{_desktopdir}/qfaktury.desktop
%{_pixmapsdir}/qfaktury*.png
