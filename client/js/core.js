/**
 * Created by mrskull on 24.11.16.
 */

let set_ground_size = function()
{
    let
		$container = document.getElementById('CONTAINTER'),
		$header = $container.querySelectorAll('.header')[0],
		$ground = $container.querySelectorAll('.ground')[0],
		$ground_block = $container.querySelectorAll('.ground-block')[0],
		$footer = $container.querySelectorAll('.footer-content')[0],


        window_height = window.document.body.clientHeight,
		header_height = $header.clientHeight,
		footer_height = $footer.clientHeight,
		ground_before_height = $ground.offsetTop,
		ground_height = window_height - header_height,
		ground_block_height = ground_height - footer_height - ground_before_height;

	$ground.style.height = ground_height +'px';
	$ground_block.style.minHeight = ground_block_height +'px';
};

window.addEventListener('load', set_ground_size);

window.addEventListener('resize', set_ground_size);