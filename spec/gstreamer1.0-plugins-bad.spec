%define majorminor   1.0
%define gstreamer    gstreamer

Summary:     GStreamer streaming media framework "bad" plug-ins
Name:        %{gstreamer}%{majorminor}-plugins-bad
Version:    1.4.5
Release:     1
License:     LGPLv2+
Group:       Applications/Multimedia
URL:         http://gstreamer.freedesktop.org/
Source:      http://gstreamer.freedesktop.org/src/gst-plugins-bad/gstreamer1.0-plugins-bad-%{version}.tar.xz
#Patch1:      0001-Set-video-branch-to-NULL-after-finishing-video-recor.patch
#Patch2:      0002-Keep-video-branch-in-NULL-state.patch
#Patch3:      0003-photography-add-missing-vmethods.patch
#Patch4:      0004-camerabin-install-GST_PHOTOGRAPHY_PROP_EXPOSURE_MODE.patch
#Patch5:      0005-Downgrade-mpeg4videoparse-to-prevent-it-from-being-p.patch
#Patch6:      0001-camerabin-update-zoom-param-spec-if-video-source-cha.patch
Requires:      orc >= 0.4.18
BuildRequires: pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires: check
BuildRequires: pkgconfig(libexif)
BuildRequires: pkgconfig(orc-0.4) >= 0.4.18
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(libgcrypt)
BuildRequires: pkgconfig(vo-aacenc)
BuildRequires: python
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: gettext-devel

%description
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

%prep
%setup -q -n gst-plugins-bad-1.4.5
#%patch1 -p1
#%patch2 -p1
#%patch3 -p1
#%patch4 -p1
#%patch5 -p1
#%patch6 -p1

%build
#NOCONFIGURE=1 ./autogen.sh

%configure --enable-quicktime --enable-uvch264 --enable-wayland --enable-egl --disable-static --enable-shared

make %{?jobs:-j%jobs}

%install
%make_install

# Clean out files that should not be part of the rpm.
rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
rm -fr $RPM_BUILD_ROOT%{_datadir}/gtk-doc

rm -rf ${RPM_BUILD_ROOT}/usr/include/gstreamer-1.0
rm -rf ${RPM_BUILD_ROOT}/usr/share/locale
rm -rf ${RPM_BUILD_ROOT}/usr/lib/pkgconfig
rm -rf ${RPM_BUILD_ROOT}/usr/lib/debug
rm -rf ${RPM_BUILD_ROOT}/usr/lib/debug/.build-id
rm -f ${RPM_BUILD_ROOT}/usr/lib/debug/usr/lib/gstreamer-1.0/libgstbz2.so.debug

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
/usr/lib/gstreamer-1.0/libgstaccurip.so
/usr/lib/gstreamer-1.0/libgstadpcmdec.so
/usr/lib/gstreamer-1.0/libgstadpcmenc.so
/usr/lib/gstreamer-1.0/libgstaiff.so
/usr/lib/gstreamer-1.0/libgstasfmux.so
/usr/lib/gstreamer-1.0/libgstaudiofxbad.so
/usr/lib/gstreamer-1.0/libgstaudiovisualizers.so
/usr/lib/gstreamer-1.0/libgstautoconvert.so
/usr/lib/gstreamer-1.0/libgstbayer.so
/usr/lib/gstreamer-1.0/libgstcoloreffects.so
/usr/lib/gstreamer-1.0/libgstdataurisrc.so
/usr/lib/gstreamer-1.0/libgstdebugutilsbad.so
/usr/lib/gstreamer-1.0/libgstdecklink.so
/usr/lib/gstreamer-1.0/libgstdvb.so
/usr/lib/gstreamer-1.0/libgstdvbsuboverlay.so
/usr/lib/gstreamer-1.0/libgstdvdspu.so
/usr/lib/gstreamer-1.0/libgstfbdevsink.so
/usr/lib/gstreamer-1.0/libgstfestival.so
/usr/lib/gstreamer-1.0/libgstfieldanalysis.so
/usr/lib/gstreamer-1.0/libgstfreeverb.so
/usr/lib/gstreamer-1.0/libgstfrei0r.so
/usr/lib/gstreamer-1.0/libgstgaudieffects.so
/usr/lib/gstreamer-1.0/libgstgdp.so
/usr/lib/gstreamer-1.0/libgstgeometrictransform.so
/usr/lib/gstreamer-1.0/libgstid3tag.so
/usr/lib/gstreamer-1.0/libgstinter.so
/usr/lib/gstreamer-1.0/libgstinterlace.so
/usr/lib/gstreamer-1.0/libgstivfparse.so
/usr/lib/gstreamer-1.0/libgstivtc.so
/usr/lib/gstreamer-1.0/libgstjp2kdecimator.so
/usr/lib/gstreamer-1.0/libgstliveadder.so
/usr/lib/gstreamer-1.0/libgstmidi.so
/usr/lib/gstreamer-1.0/libgstmpegpsdemux.so
/usr/lib/gstreamer-1.0/libgstmpegpsmux.so
/usr/lib/gstreamer-1.0/libgstmpegtsmux.so
/usr/lib/gstreamer-1.0/libgstmxf.so
/usr/lib/gstreamer-1.0/libgstopengl.so
/usr/lib/gstreamer-1.0/libgstpcapparse.so
/usr/lib/gstreamer-1.0/libgstpnm.so
/usr/lib/gstreamer-1.0/libgstremovesilence.so
/usr/lib/gstreamer-1.0/libgstrfbsrc.so
/usr/lib/gstreamer-1.0/libgstsdpelem.so
/usr/lib/gstreamer-1.0/libgstsegmentclip.so
/usr/lib/gstreamer-1.0/libgstsiren.so
/usr/lib/gstreamer-1.0/libgstsmooth.so
/usr/lib/gstreamer-1.0/libgstspeed.so
/usr/lib/gstreamer-1.0/libgststereo.so
/usr/lib/gstreamer-1.0/libgstsubenc.so
/usr/lib/gstreamer-1.0/libgstuvch264.so
/usr/lib/gstreamer-1.0/libgstvideofiltersbad.so
/usr/lib/gstreamer-1.0/libgstvideosignal.so
/usr/lib/gstreamer-1.0/libgstvmnc.so
/usr/lib/gstreamer-1.0/libgstwaylandsink.so
/usr/lib/gstreamer-1.0/libgsty4mdec.so
/usr/lib/gstreamer-1.0/libgstyadif.so
/usr/lib/libgstbadbase-1.0.so
/usr/lib/libgstbadvideo-1.0.so
/usr/lib/libgstbasecamerabinsrc-1.0.so
/usr/lib/libgstcodecparsers-1.0.so
/usr/lib/libgstgl-1.0.so
/usr/lib/libgstgl-1.0.so.0
/usr/lib/libgstgl-1.0.so.0.405.0
/usr/lib/libgstinsertbin-1.0.so
/usr/lib/libgstmpegts-1.0.so
/usr/lib/libgstphotography-1.0.so
/usr/lib/libgsturidownloader-1.0.so
/usr/lib/libgstwayland-1.0.so
/usr/lib/libgstwayland-1.0.so.0
/usr/lib/libgstwayland-1.0.so.0.405.0
/usr/lib/gstreamer-1.0/libgstaudiomixer.so
/usr/lib/gstreamer-1.0/libgstcamerabin2.so
/usr/lib/gstreamer-1.0/libgstcompositor.so
/usr/lib/gstreamer-1.0/libgstfragmented.so
/usr/lib/gstreamer-1.0/libgstjpegformat.so
/usr/lib/gstreamer-1.0/libgstmpegtsdemux.so
/usr/lib/gstreamer-1.0/libgstrawparse.so
/usr/lib/gstreamer-1.0/libgstshm.so
/usr/lib/gstreamer-1.0/libgstvideoparsersbad.so
/usr/lib/gstreamer-1.0/libgstvoaacenc.so
/usr/lib/libgstbadbase-1.0.so.0
/usr/lib/libgstbadbase-1.0.so.0.405.0
/usr/lib/libgstbadvideo-1.0.so.0
/usr/lib/libgstbadvideo-1.0.so.0.405.0
/usr/lib/libgstbasecamerabinsrc-1.0.so.0
/usr/lib/libgstbasecamerabinsrc-1.0.so.0.405.0
/usr/lib/libgstcodecparsers-1.0.so.0
/usr/lib/libgstcodecparsers-1.0.so.0.405.0
/usr/lib/libgstinsertbin-1.0.so.0
/usr/lib/libgstinsertbin-1.0.so.0.405.0
/usr/lib/libgstmpegts-1.0.so.0
/usr/lib/libgstmpegts-1.0.so.0.405.0
/usr/lib/libgstphotography-1.0.so.0
/usr/lib/libgstphotography-1.0.so.0.405.0
/usr/lib/libgsturidownloader-1.0.so.0
/usr/lib/libgsturidownloader-1.0.so.0.405.0
/usr/lib/gstreamer-1.0/libgstbz2.so

