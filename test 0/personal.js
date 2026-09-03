
    document.getElementById('year').textContent = new Date().getFullYear();

    // 滚动渐现
    const io = new IntersectionObserver(entries => {
      entries.forEach(e => { if(e.isIntersecting) e.target.classList.add('show'); });
    }, { threshold: .1 });
    document.querySelectorAll('.fade').forEach(s => io.observe(s));

    // 移动端菜单关闭
    document.querySelectorAll('.nav-links a').forEach(link => {
      link.addEventListener('click', () => {
        document.querySelector('.nav-links').classList.remove('active');
      });
    });
