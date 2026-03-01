% rebase('layout.tpl', title=title, year=year)

<div class="music-container">
	<p class="heading-text">Популярные релизы</p>
	<div class="music-scroll-row">
		<a href="/music/zmiShare" class="music-card {{'active' if selected_track == 'zmiShare' else ''}}">
			<img src="/static/images/musicPage/zhmiShareImage.png"/>
			<p class="heading-text">ЖмиShare</p>
			<p class="regular-text">5opka, Mellsher</p>			
		</a>
		<a href="/music/42" class="music-card {{'active' if selected_track == '42' else ''}}">
			<img src="/static/images/musicPage/42Image.png"/>
			<p class="heading-text">42</p>
			<p class="regular-text">5opka, 6055</p>			
		</a>
		<a href="/music/venomBoy" class="music-card {{'active' if selected_track == 'venomBoy' else ''}}">
			<img src="/static/images/musicPage/venomBoyImage.png"/>
			<p class="heading-text">Веном Boy</p>
			<p class="regular-text">Дмитрий Маликов, 5opka</p>			
		</a>
		<a href="/music/1000zhizney" class="music-card {{'active' if selected_track == '1000zhizney' else ''}}">
			<img src="/static/images/musicPage/1000zhizneyImage.png"/>
			<p class="heading-text">1000 жизней</p>
			<p class="regular-text">5opka</p>			
		</a>
		<a href="/music/slavaBossu" class="music-card {{'active' if selected_track == 'slavaBossu' else ''}}">
			<img src="/static/images/musicPage/slavaBossuImage.jpg"/>
			<p class="heading-text">Слава боссу</p>
			<p class="regular-text">5opka</p>			
		</a>
		<a href="/music/golovolomka" class="music-card {{'active' if selected_track == 'golovolomka' else ''}}">
			<img src="/static/images/musicPage/golovolomkaImage.jpg"/>
			<p class="heading-text">Головоломка</p>
			<p class="regular-text">5opka</p>			
		</a>
	</div>

	{{!music_content}}
</div>

<script>
window.addEventListener('load', function() {
    var container = document.querySelector('.music-scroll-row');
    if (container) {
        var containerWidth = container.clientWidth;
        var scrollWidth = container.scrollWidth;
        var maxScroll = scrollWidth - containerWidth;
        var centerScroll = maxScroll / 2;
        container.scrollLeft = centerScroll;
    }
});
</script>