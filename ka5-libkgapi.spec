%define		kdeappsver	18.12.1
%define		qtver		5.9.0
%define		kaname		libkgapi
Summary:	libkgapi
Name:		ka5-%{kaname}
Version:	18.12.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	4c1586446861dce28820711ae8ecaa7e
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Network-devel
BuildRequires:	Qt5Positioning-devel >= 5.11.1
BuildRequires:	Qt5PrintSupport-devel >= 5.11.1
BuildRequires:	Qt5Qml-devel >= 5.11.1
BuildRequires:	Qt5Quick-devel >= 5.11.1
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5WebChannel-devel >= 5.11.1
BuildRequires:	Qt5WebEngine-devel >= 5.11.1
BuildRequires:	Qt5Widgets-devel
BuildRequires:	Qt5Xml-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	cyrus-sasl-devel
BuildRequires:	gettext-devel
BuildRequires:	ka5-kcalcore-devel >= %{kdeappsver}
BuildRequires:	ka5-kcontacts-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= 5.53.0
BuildRequires:	kf5-kio-devel >= 5.51.0
BuildRequires:	kf5-kwallet-devel >= 5.51.0
BuildRequires:	kf5-kwindowsystem-devel >= 5.51.0
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LibKGAPI is a KDE-based library for accessing various Google services
via their public API.

%package devel
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kaname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kaname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kaname}.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kaname}_qt --with-qm --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}_qt.lang
%defattr(644,root,root,755)
/etc/xdg/libkgapi.categories
%attr(755,root,root) %ghost %{_libdir}/libKPimGAPIBlogger.so.5
%attr(755,root,root) %{_libdir}/libKPimGAPIBlogger.so.5.*.*
%attr(755,root,root) %ghost %{_libdir}/libKPimGAPICalendar.so.5
%attr(755,root,root) %{_libdir}/libKPimGAPICalendar.so.5.*.*
%attr(755,root,root) %ghost %{_libdir}/libKPimGAPIContacts.so.5
%attr(755,root,root) %{_libdir}/libKPimGAPIContacts.so.5.*.*
%attr(755,root,root) %ghost %{_libdir}/libKPimGAPICore.so.5
%attr(755,root,root) %{_libdir}/libKPimGAPICore.so.5.*.*
%attr(755,root,root) %ghost %{_libdir}/libKPimGAPIDrive.so.5
%attr(755,root,root) %{_libdir}/libKPimGAPIDrive.so.5.*.*
%attr(755,root,root) %ghost %{_libdir}/libKPimGAPILatitude.so.5
%attr(755,root,root) %{_libdir}/libKPimGAPILatitude.so.5.*.*
%attr(755,root,root) %ghost %{_libdir}/libKPimGAPIMaps.so.5
%attr(755,root,root) %{_libdir}/libKPimGAPIMaps.so.5.*.*
%attr(755,root,root) %ghost %{_libdir}/libKPimGAPITasks.so.5
%attr(755,root,root) %{_libdir}/libKPimGAPITasks.so.5.*.*
%attr(755,root,root) %ghost %{_libdir}/sasl2/libkdexoauth2.so.3
%attr(755,root,root) %{_libdir}/sasl2/libkdexoauth2.so.3.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/KPim/KGAPI
%{_includedir}/KPim/kgapi_version.h
%{_libdir}/cmake/KPimGAPI
%attr(755,root,root) %{_libdir}/libKPimGAPIBlogger.so
%attr(755,root,root) %{_libdir}/libKPimGAPICalendar.so
%attr(755,root,root) %{_libdir}/libKPimGAPIContacts.so
%attr(755,root,root) %{_libdir}/libKPimGAPICore.so
%attr(755,root,root) %{_libdir}/libKPimGAPIDrive.so
%attr(755,root,root) %{_libdir}/libKPimGAPIMaps.so
%attr(755,root,root) %{_libdir}/libKPimGAPILatitude.so
%attr(755,root,root) %{_libdir}/libKPimGAPITasks.so
%attr(755,root,root) %{_libdir}/sasl2/libkdexoauth2.so
%{_libdir}/qt5/mkspecs/modules/qt_KGAPIBlogger.pri
%{_libdir}/qt5/mkspecs/modules/qt_KGAPICalendar.pri
%{_libdir}/qt5/mkspecs/modules/qt_KGAPIContacts.pri
%{_libdir}/qt5/mkspecs/modules/qt_KGAPICore.pri
%{_libdir}/qt5/mkspecs/modules/qt_KGAPIDrive.pri
%{_libdir}/qt5/mkspecs/modules/qt_KGAPILatitude.pri
%{_libdir}/qt5/mkspecs/modules/qt_KGAPIMaps.pri
%{_libdir}/qt5/mkspecs/modules/qt_KGAPITasks.pri
