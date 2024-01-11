Name: ipcalc
Version: 0.2.4
Release: 4%{?dist}
Summary: IP network address calculator

# This is an updated version of ipcalc originally found
# in Fedora's initscripts at:
# https://fedorahosted.org/releases/i/n/initscripts/

License: GPLv2+
URL: https://gitlab.com/ipcalc/ipcalc
Source0: https://gitlab.com/ipcalc/ipcalc/-/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc, git, libmaxminddb-devel
Recommends:    libmaxminddb, geolite2-city, geolite2-country

# Explicitly conflict with older initscript packages that ship ipcalc
Conflicts: initscripts < 9.63
# Obsolete ipcalculator
Obsoletes:  ipcalculator < 0.41-20

Patch1: 0001-fix-segfault-in-env-without-libmaxmind.so.patch
Patch2: 0002-add-support-for-RFC3021.patch

%description
ipcalc provides a simple way to calculate IP information for a host
or network. Depending on the options specified, it may be used to provide
IP network information in human readable format, in a format suitable for
parsing in scripts, generate random private addresses, resolve an IP address,
or check the validity of an address.

%prep
%autosetup -S git

%build
CFLAGS="${CFLAGS:-%optflags} $RPM_LD_FLAGS" \
  USE_RUNTIME_LINKING=yes USE_GEOIP=no USE_MAXMIND=yes LIBPATH=%{_libdir} make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_bindir}
install -p -m 755 ipcalc %{buildroot}%{_bindir}/
mkdir -p -m 755 %{buildroot}%{_mandir}/man1
install -p -m 644 ipcalc.1 %{buildroot}%{_mandir}/man1

%check
make check

%files

%{_bindir}/ipcalc
%license COPYING
%doc README.md
%{_mandir}/man1/ipcalc.1*

%changelog
* Thu Oct 10 2019 Martin Osvald <mosvald@redhat.com> - 0.2.4-4
- Add support for RFC3021 (#1638834)

* Fri Aug 03 2018 Martin Sehnoutka <msehnout@redhat.com> - 0.2.4-3
- Fix segfault in the container environment

* Thu Aug 02 2018 Martin Sehnoutka <msehnout@redhat.com> - 0.2.4-2
- Recommend databases

* Tue Jul 24 2018 Martin Sehnoutka <msehnout@redhat.com> - 0.2.4-1
- Resolves: #1601400 with rebase to 0.2.4

* Fri Feb  9 2018 Florian Weimer <fweimer@redhat.com> - 0.2.2-4
- Another attempt at injecting LDFLAGS

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Feb  1 2018 Florian Weimer <fweimer@redhat.com> - 0.2.2-2
- Build with linker flags from redhat-rpm-config

* Tue Jan 02 2018 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.2.2-1
- New upstream release

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.2.0-1
- New upstream release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun 15 2016 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.1.8-1
- New upstream release

* Fri Apr  1 2016 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.1.7-1
- New upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec  8 2015 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.1.6-1
- New upstream release

* Wed Oct 14 2015 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.1.4-2
- Corrected issue on --all-info

* Wed Oct 14 2015 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.1.4-1
- New upstream release

* Tue Oct  6 2015 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.1.3-1
- New upstream release
- Prints GeoIP information on generic info

* Mon Sep 21 2015 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.1.2-3
- This package obsoletes ipcalculator

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun  9 2015 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.1.2-1
- New upstream release

* Tue May 19 2015 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.1.1-1
- Compatibility fixes (allow a mask of 0)

* Mon May 18 2015 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.1.0-1
- First independent release outside initscripts
