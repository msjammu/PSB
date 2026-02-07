// Contact info obfuscation - prevents bots from scraping email/phone
(function () {
    var u = 'Info';
    var d = 'punjabischoolbothell';
    var t = 'org';
    var e = u + '@' + d + '.' + t;
    var p1 = '+1 (425)';
    var p2 = ' 233-';
    var p3 = '8319';
    var p = p1 + p2 + p3;
    var pr = '+14252338319';

    // Footer contact
    var fe = document.getElementById('footer-email');
    if (fe) {
        fe.href = 'mai' + 'lto:' + e;
        fe.innerHTML = '<i class="fas fa-envelope me-2"></i>' + e;
    }
    var fp = document.getElementById('footer-phone');
    if (fp) {
        fp.href = 'te' + 'l:' + pr;
        fp.innerHTML = '<i class="fas fa-phone me-2"></i>' + p;
    }

    // Enroll page CTA buttons
    var ce = document.getElementById('cta-email');
    if (ce) {
        ce.href = 'mai' + 'lto:' + e;
    }
    var cp = document.getElementById('cta-phone');
    if (cp) {
        cp.href = 'te' + 'l:' + pr;
    }
})();
