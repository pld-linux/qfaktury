Summary:	Free software for creating, managing, and printing invoices
Summary(pl.UTF-8):	Darmowy i wszechstronny system fakturujący
Name:		qfaktury
Version:	0.5.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/qfaktury/%{name}-%{version}-Source.tar.gz
# Source0-md5:	1ae6a9826c51fd6597500e6f39cdc7fd
Patch0:		%{name}-desktop.patch
URL:		http://qfaktury.sourceforge.net/
BuildRequires:	cmake
BuildRequires:	Qt3Support-devel
BuildRequires:	QtXml-devel
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
%setup -q -n %{name}-%{version}-Source
#%patch0 -p1

%build
rm -rf build
mkdir build
cd build
export CXXFLAGS="%{rpmcxxflags}"
%cmake .. \
	-DCMAKE_INSTALL_PREFIX="%{_prefix}" \
	%{?debug:-DCMAKE_BUILD_TYPE="Debug"}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

# it's not used anyway...
cp -r share/qfaktury $RPM_BUILD_ROOT%{_datadir}
install share/qfaktury/icons/qfaktury.desktop $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ReadMe.txt
%attr(755,root,root) %{_bindir}/qfaktury
%{_datadir}/qfaktury
%{_desktopdir}/qfaktury.desktop
