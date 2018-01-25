import requests, re




source = '''
<!DOCTYPE html>
<html lang="ko">










<head>
		
	
	
	
	
	
	

	<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
	<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
	<title>멜론차트>멜론 TOP 100>실시간>멜론</title>
	<meta name="keywords" content="음악서비스, 멜론차트, 멜론TOP100, 최신음악, 인기가요, 뮤직비디오, 앨범, 플레이어, 스트리밍, 다운로드, 아티스트플러스, 아티스트채널" />
	<meta name="description" content="국내 최대 1,000만곡 확보 No.1 음악사이트, 멜론! 최신음악과 실시간 차트는 기본, 내 취향을 아는 똑똑한 추천 라디오, 내가 좋아하는 아티스트의 새로운 소식까지 함께 즐겨보세요." />
	<meta name="naver-site-verification" content="f13fc46b807bef984aa341efeb1adec8de12264c"/>
	<meta property="fb:app_id" content="357952407588971"/>
	<meta property="og:title" content="Melon"/>
	<meta property="og:image" content="http://cdnimg.melon.co.kr/resource/image/web/common/logo_melon142x99.png"/>
	<meta property="og:description" content="음악이 필요한 순간, 멜론"/>
	<meta property="og:url" content="http://www.melon.com/chart/index.htm"/>
	<meta property="og:type" content="website"/>
	<meta name="viewport" content="width=device-width"/>
	<link rel="shortcut icon" type="image/x-icon" href="/favicon.ico?2" id="favicon"/>
	
		
		
		
		
		
	
	<script type="text/javascript">
		checkWin8Metro();
		function checkWin8Metro(){
			var userAgent = navigator.userAgent.toLowerCase();
			var canRunActiveX = false;
			try
			{
				canRunActiveX = !!new ActiveXObject("htmlfile");
			}
			catch (e)
			{
				canRunActiveX = false;
			}
			if ((userAgent.indexOf("windows nt 6.2") >= 0 || userAgent.indexOf("windows nt 6.3") >= 0 ) && userAgent.indexOf("msie") >= 0)
			{
				// windows 8
				if (canRunActiveX == false)
				{
					document.location.href = "http://t.melon.com";
				}
			}
		}
	</script>
	
	
	

		
	<link rel="stylesheet" href="http://cdnimg.melon.co.kr/static/web/resource/style/w1/8b/9/1y1v0s21vgv.css" type="text/css" />
	<link rel="stylesheet" href="http://cdnimg.melon.co.kr/static/web/resource/style/w1/5r/m/14j3tr44urn.css" type="text/css" />

	<!-- 댓글 css 파일 네임 변경 -->
    <link rel="stylesheet" href="http://cdnimg.melon.co.kr/static/web/resource/style/w1/qd/e/uolshpokn9.css" type="text/css" /> 
  	
  		
  		
			<link rel="stylesheet" href="/resource/style/web/chart/melonweb_chart_4x.css" type="text/css" />
  		
  	
  	
  	<link rel="stylesheet" href="http://cdnimg.melon.co.kr/static/web/resource/style/w1/g6/0/kvg1wtiobj.css" type="text/css" />
	<link href="https://fonts.googleapis.com/css?family=Nunito:400" rel="stylesheet">
  	
	
	
	<script type="text/javascript" src="/resource/script/web/common/jquery-1.9.1.min.js"></script>
	<script type="text/javascript" src="//member.melon.com/resource/script/web/member/melonweb_member_external.js?tm=20180115"></script>
	<script type="text/javascript" src="http://cdnimg.melon.co.kr/static/web/resource/script/w1/g8/u/kv5d3h4q8t.js"></script> 
	<script type="text/javascript">


	MelonPersonal.init();

	(function() {
		WEBPOCIMG = {
			defaultImg : function(obj, width){
				if(width == null || width == '') width = $(obj).width();
				if(width == 0) width = 500;
				var thumbType = "_500";
				//가장 큰사이즈로 리사이즈함
				var thumbType = "_500";
				var defaultImg = "http://cdnimg.melon.co.kr/resource/image/web/default/noAlbum" + thumbType + "_160727.jpg/melon/resize/" + width;
				if(obj.src != defaultImg){
					obj.src = defaultImg;
				}
			},

			defaultAlbumImg : function(obj, width){
				if(width == null || width == '') width = $(obj).width();
				if(width == 0) width = 500;
				//가장 큰사이즈로 리사이즈함
				var thumbType = "_500";
				var defaultImg = "http://cdnimg.melon.co.kr/resource/image/web/default/noAlbum" + thumbType + "_160727.jpg/melon/resize/" + width;
				if(obj.src != defaultImg){
					obj.src = defaultImg;
				}
			},

			defaultArtistImg : function(obj, width){
				if(width == null || width == '') width = $(obj).width();
				if(width == 0) width = 300;
				//가장 큰사이즈로 리사이즈함
				var thumbType = "_300";
				var defaultImg = "http://cdnimg.melon.co.kr/resource/image/web/default/noArtist" + thumbType + "_160727.jpg/melon/resize/" + width;
				if(obj.src != defaultImg){
					obj.src = defaultImg;
				}
			},
			defaultDjImg : function(obj){
			},
			defaultMvImg : function(obj, width, height){
				if(width == null || width == '') width = $(obj).width();
				if(height == null || height == '') height = $(obj).height();

				var ratio43 = Math.floor((4/3)*10)/10;
				var ratio169 = Math.floor((16/9)*10)/10;
				var ratioObj = Math.floor((width/height)*10)/10;

				var ratio = "4x3";
				if(ratioObj == ratio43){
					ratio = "4x3"; //contentsType = "mv43";
				} else if(ratioObj == ratio169){
					ratio = "16x9"; //contentsType = "mv169";
				} else {
					if(ratioObj > 1.5) ratio = "16x9";
					else ratio = "4x3";
				}

				if(width == 0) width = 640;
				if(height == 0) ratio = "16x9";

				//가장 큰사이즈로 리사이즈함
				var thumbType = "_" + ratio + "_640";
				var defaultImg = "http://cdnimg.melon.co.kr/resource/image/web/default/noMovie" + thumbType + "_160727.jpg/melon/resize/" + width;
				if(obj.src != defaultImg){
					obj.src = defaultImg;
				}
			},
			defaultPlaylistImg : function(obj, width){
				if(width == null || width == '') width = $(obj).width();
				if(width == 0) width = 500;
				//가장 큰사이즈로 리사이즈함
				var thumbType = "_500";
				var defaultImg = "http://cdnimg.melon.co.kr/resource/image/web/default/noAlbum" + thumbType + "_160727.jpg/melon/resize/" + width;
				if(obj.src != defaultImg){
					obj.src = defaultImg;
				}
			},
			defaultMemberImg : function(obj, width){
				if(width == null || width == '') width = $(obj).width();
				if(width == 0) width = 300;
				//가장 큰사이즈로 리사이즈함
				var thumbType = "_300";
				var defaultImg = "http://cdnimg.melon.co.kr/resource/image/web/default/noArtist" + thumbType + "_160727.jpg/melon/resize/" + width;
				if(obj.src != defaultImg){
					obj.src = defaultImg;
				}
			},
			defaultPhotoImg : function(obj, width){
				if(width == null || width == '') width = $(obj).width();
				if(width == 0) width = 500;
				//가장 큰사이즈로 리사이즈함
				var thumbType = "_500";
				var defaultImg = "http://cdnimg.melon.co.kr/resource/image/web/default/noAlbum" + thumbType + "_160727.jpg/melon/resize/" + width;
				if(obj.src != defaultImg){
					obj.src = defaultImg;
				}
			},
			defaultShopImg : function(obj, width){
				if(width == null || width == '') width = $(obj).width();
				if(width == 0) width = 256;
				//가장 큰사이즈로 리사이즈함
				var thumbType = "_256";
				var defaultImg = "http://cdnimg.melon.co.kr/resource/image/web/default/noProduct" + thumbType + "_160727.jpg/melon/resize/" + width;
				if(obj.src != defaultImg){
					obj.src = defaultImg;
				}
			},
			defaultShowwingImg : function(obj, width){
				if(width == null || width == '') width = $(obj).width();

				var thumbType = "_256";
				if(width > 0 && width <= 300){
					thumbType = "_256";
				} else {
					thumbType = "_313";//추후 조절값
				}
				var altSrc = "http://cdnimg.melon.co.kr/resource/image/web/default/noShowing" + thumbType + ".jpg";
				if(obj.src != altSrc){
					obj.src = altSrc;
				}
			},
			defaultTicketImg : function(obj, width){
				if(width == null || width == '') width = $(obj).width();

				var thumbType = "_256";
				if(width > 0 && width <= 300){
					thumbType = "_256";
				} else {
					thumbType = "_313";//추후 조절값
				}
				var altSrc = "http://cdnimg.melon.co.kr/resource/image/web/default/noTicket" + thumbType + ".png";
				if(obj.src != altSrc){
					obj.src = altSrc;
				}
			},
			defaultSmartRadioImg : function(obj, width){
				if(width == null || width == '') width = $(obj).width();
				var defaultImg = "http://cdnimg.melon.co.kr/resource/image/web/default/noSmartradio_59_160727.jpg/melon/resize/" + width;
				if(obj.src != defaultImg){
					obj.src = defaultImg;
				}
			},
			defaultConcertImg : function(obj, width){
				if(width == null || width == '') width = $(obj).width();
				var defaultImg = "http://cdnimg.melon.co.kr/resource/image/web/default/noAlbum_114_160727.jpg/melon/resize/" + width;
				if(obj.src != defaultImg){
					obj.src = defaultImg;
				}
			}
		}
		,WEBELLIPSIS = {
			ellipsis : function(ellipsisName,moreClassName,eWidth){
		        //아티스트 더보기
		        var arObj = $('.' + ellipsisName);
		        for(var i = 0; i < arObj.length; i++){
		            if (arObj.eq(i).width() > eWidth ){
		                arObj.eq(i).parent().parent().parent().find('.' + moreClassName).show();
		            }
		        }
			}
		}
	})();
	</script>
</head>

<body>
<div id="wrap">
	<div id="skip_nav">skip navigation
		<ul>
			<li><a href="#gnb_menu">메뉴</a></li>
			<li><a href="#id_box">마이영역</a></li>
			<li><a href="#conts_section">본문</a></li>
			<li><a href="#footer">하단 정보</a></li>
		</ul>
	</div>

	<!--  header -->
	
	<div id="header" class="gnb2_expn">
		<div id="header_wrap" class="my_fold">  <!-- 1024이상 마이영역 접었을때 클래스 my_fold 추가 -->
			<div id="gnb" class="clfix">
				<!-- 상단 빠른 메뉴 -->
				<div id="util_menu">
					<p class="none">상단 빠른 메뉴</p>
					<div class="top_left">
						<ul class="clfix">
							
							<li class="first_child d_melon_ticket"><a href="http://ticket.melon.com/main/index.htm" title="멜론 티켓" class="menu01 mlog" data="LOG_PRT_CODE=1&MENU_PRT_CODE=0&MENU_ID_LV1=&CLICK_AREA_PRT_CODE=V08&ACTION_AF_CLICK=V1"><span>멜론 티켓</span></a></li>
							
							<li><a href="http://aztweb.melon.com/aztalk/guide/web/main.htm" title="멜론 아지톡" class="menu03 mlog" data="LOG_PRT_CODE=1&MENU_PRT_CODE=0&MENU_ID_LV1=&CLICK_AREA_PRT_CODE=V05&ACTION_AF_CLICK=V1"><span>멜론 아지톡</span></a></li><!-- 161206 -->
						</ul>
					</div>
					<!-- 140603_수정 -->
					<div class="top_right ">
						<ul class="clfix">
							
							<li class="first_child"><a href="/commerce/pamphlet/web/sale_listMainView.htm" title="이용권구매" class="menu01 mlog" data="LOG_PRT_CODE=1&MENU_PRT_CODE=0&MENU_ID_LV1=&CLICK_AREA_PRT_CODE=B01&ACTION_AF_CLICK=V1"><span>이용권구매</span></a></li>
							
							<li><a href="/event/vip/index.htm" title="VIP혜택관" class="menu02 mlog" data="LOG_PRT_CODE=1&MENU_PRT_CODE=0&MENU_ID_LV1=&CLICK_AREA_PRT_CODE=V06&ACTION_AF_CLICK=V1"><span>VIP혜택관</span></a></li>
							
							<li class="last_child"><a href="/event/index.htm" title="이벤트" class="menu03 mlog" data="LOG_PRT_CODE=1&MENU_PRT_CODE=0&MENU_ID_LV1=&CLICK_AREA_PRT_CODE=B03&ACTION_AF_CLICK=V1"><span>이벤트</span></a></li>
						</ul>
					</div>
					<!-- //140603_수정 -->
				</div>
				<!-- //상단 빠른 메뉴 -->

				<!-- 140603_수정 -->
				
				<h1><a href="http://www.melon.com/index.htm" title="MelOn 로고 - 홈으로 이동" class="mlog" data="LOG_PRT_CODE=1&MENU_PRT_CODE=0&MENU_ID_LV1=&CLICK_AREA_PRT_CODE=M01&ACTION_AF_CLICK=V1"><img width="142" height="99" src="http://cdnimg.melon.co.kr/resource/image/web/common/logo_melon142x99.png" alt="MelOn 로고 이미지"/></a></h1>
				
				<!-- //140603_수정 -->
				<!-- 통합검색 영역 -->
				<fieldset>
					<legend>통합검색영역</legend>
					<input type="text" title="검색 입력 편집창" placeholder="" name="" id="top_search" style="width:249px" onkeypress="if(event.keyCode == 13){goSearch();}"/><input type="hidden" name="keywordLink" id="keywordLink" value="" />
					<button type="button" style="display: none;" id="top_search_autocomplete_toggle" class="btn_icon btn_auto close" title="자동검색 펼침"><span class="odd_span">자동검색 펼침</span></button> <!-- open/close 클래스 사용 -->
					<button type="button" class="btn_icon search_m" title="검색"><span class="odd_span">검색</span></button>
					<div class="auto_complete" id="top_search_autocomplete"><div class="auto_complete_cont" style="display:block;"><!-- 자동완성 레이어 --></div></div>
					<div class="auto_complete" id="top_search_autocomplete_template" style="display: none;"> <!-- 자동완성 레이어 템플릿 -->
						<!-- 텍스트 결과 -->
						<ul class="text_result">
							<li><a href="#" class="autocomplete-label"></a></li>
						</ul>
						<!-- 섬네일 결과 -->
						<ul class="thumb_result">
							<li class="cate"></li>
							<li class="class02">
								<a href="#">
									<span class="thumb_40">
										<span class="thumb_frame"></span>
										<img class="autocomplete-img" width="40" height="40" alt="">
									</span>
									<div class="info">
										<span class="autocomplete-label"></span><br/>
										<span><span class="f11 autocomplete-info"></span></span>
									</div>
								</a>
							</li>
						</ul>
						<!-- 검색어가 없을 때 -->
						<ul class="text_result">
							<li class="result_none">
								<span>해당글자로 시작하는 단어가 없습니다.</span>
							</li>
						</ul>
					</div>
				</fieldset>
				<form style="display: none" id="searchFrm" method="get" action="">
					<input type="hidden" name="q"/>
					<input type="hidden" name="section"/>
				</form>
				<!-- //통합검색 영역 -->

				<!-- 실시간 검색어 -->
				<div class="realtime_soar_keyword">
					<!-- 140519_수정 -->
					<a href="http://www.melon.com/search/trend/index.htm" class="title">급상승 키워드</a>
					<!-- //140519_수정 -->
					<div class="keyword_overlay">
						<ol style="overflow:hidden; height:20px;">
							<!-- 롤링 영역
							<li>
								<div style="top:;">
									<strong class="order bg2 on"><span class="none">1 위</span></strong>
									<a href="#" class="ellipsis" title="something">something</a>
									<span class="wrap_rank">
										<span class="icon_up">순위상승수</span><span>139</span>
										<!- <span class="icon_rank_new">새진입</span>
									</span>
								</div>
							</li>
							//롤링 영역 -->
						</ol>
						<!-- 140423_추가 -->
						<a href="http://www.melon.com/search/trend/index.htm" class="keyword_more" title="실시간 순위"><span>더보기 <span></span></span></a>
						<!-- //140423_추가 -->
					</div>
					<!-- 140423_삭제 -->
					<!-- <a href="#" class="d_btn_ctrl pause" title="이벤트 일시정지"><span><span class="none">일시정지</span></span></a> -->
					<!-- //140423_삭제 -->
				</div>
				<!-- //실시간 검색어 -->

				<!-- 배너 영역 -->
				<div class="cmn_banner"></div>

                <script type="text/javascript">
				MelonPersonal.printLayout();
				</script>
			</div>
            <!-- 140314_gnb마크업 수정 -->
			<div id="gnb_menu">
				<ul>
					<li class="nth1 on">
						
						<a href="http://www.melon.com/chart/index.htm" class="cur_menu mlog" data="LOG_PRT_CODE=1&MENU_PRT_CODE=0&MENU_ID_LV1=&CLICK_AREA_PRT_CODE=R01&ACTION_AF_CLICK=V1"><span class="cur_status none">현재 선택된 메뉴-</span><span class="menu_bg menu01">멜론차트</span></a>
						<div class="lay_menu">
							<ul>
								<li class="first_child on"><a href="http://www.melon.com/chart/index.htm"><span class="menu_chart m1">멜론 TOP 100</span></a></li>
								<li class=""><a href="http://www.melon.com/melonaward/timeline.htm?f=c"><span class="menu_chart m2">주간 인기상</span></a></li>
								<li class=""><a href="http://www.melon.com/chart/vdo/index.htm"><span class="menu_chart m3">트렌드 차트</span></a></li>
								<li class=""><a href="http://www.melon.com/chart/genre/index.htm"><span class="menu_chart m4">장르 스타일 차트</span></a></li>
								<li class=""><a href="http://www.melon.com/chart/age/index.htm"><span class="menu_chart m5">시대별 차트</span></a></li>
							</ul>
							<div class="chart_finder">
								<button type="button" class="btn_chart_f" onclick="location.href='http://www.melon.com/chart/search/index.htm'"><span class="odd_span">차트 파인더</span></button>
							</div>							
						</div>	
					</li>
					<li class="nth2">
						
						<a href="http://www.melon.com/new/index.htm" class="cur_menu mlog" data="LOG_PRT_CODE=1&MENU_PRT_CODE=0&MENU_ID_LV1=&CLICK_AREA_PRT_CODE=C01&ACTION_AF_CLICK=V1"><span class="cur_status none">현재 선택된 메뉴-</span><span class="menu_bg menu02 ">최신</span></a>
						<div class="lay_menu">
							<ul>
								<li class="first_child"><a href="http://www.melon.com/new/index.htm"><span class="menu_new m1">최신곡</span></a></li>
								<li class=""><a href="http://www.melon.com/new/album/index.htm"><span class="menu_new m2">최신앨범</span></a></li>
								<li class=""><a href="http://www.melon.com/new/mv/index.htm"><span class="menu_new m3">최신 뮤직비디오</span></a></li>
								<!-- 160404 제거 -->
								
								<!-- // 160404 제거 -->
							</ul>							
						</div>
					</li>
					<li class="nth3">
						
						<a href="http://www.melon.com/genre/song_list.htm?gnrCode=GN0100" class="cur_menu mlog" data="LOG_PRT_CODE=1&MENU_PRT_CODE=0&MENU_ID_LV1=&CLICK_AREA_PRT_CODE=C03&ACTION_AF_CLICK=V1"><span class="cur_status none">현재 선택된 메뉴-</span><span class="menu_bg menu03">장르</span></a>
						<div class="lay_menu">
							<ul>
								<li class="first_child"><a href="http://www.melon.com/genre/song_list.htm?gnrCode=GN0100"><span class="menu_gnr nm1">한국대중음악</span></a></li>
								<li class=""><a href="http://www.melon.com/genre/song_list.htm?gnrCode=GN0900"><span class="menu_gnr nm2">해외POP음악</span></a></li>
								<li class=""><a href="http://www.melon.com/genre/song_list.htm?gnrCode=GN1500"><span class="menu_gnr nm3">그외 인기장르</span></a></li>
							</ul>
						</div>
					</li>
					<li class="nth4">
						
						<a href="http://www.melon.com/dj/today/djtoday_list.htm" class="cur_menu mlog" data="LOG_PRT_CODE=1&MENU_PRT_CODE=0&MENU_ID_LV1=&CLICK_AREA_PRT_CODE=S04&ACTION_AF_CLICK=V1"><span class="cur_status none">현재 선택된 메뉴-</span><span class="menu_bg menu04">멜론DJ</span></a>
						<div class="lay_menu">
							<ul>
								<li class="first_child"><a href="http://www.melon.com/dj/today/djtoday_list.htm"><span class="menu_dj m1">오늘은 뭘 듣지</span></a></li>
								<li class=""><a href="http://www.melon.com/dj/essential/djessential_list.htm"><span class="menu_dj m2">전문가 선곡</span></a></li>
								<li class=""><a href="http://www.melon.com/dj/themegenre/djthemegenre_list.htm"><span class="menu_dj m3">#테마장르</span></a></li>
								<li class=""><a href="http://www.melon.com/dj/powerdj/djpowerdj_list.htm"><span class="menu_dj m4">파워DJ</span></a></li>
								<li class=""><a href="http://www.melon.com/dj/chart/djchart_list.htm"><span class="menu_dj m5">인기</span></a></li>
							</ul>
						</div>	
					</li>
					<li class="nth5">
						
						<a href="http://www.melon.com/tv/index.htm" class="cur_menu mlog" data="LOG_PRT_CODE=1&MENU_PRT_CODE=0&MENU_ID_LV1=&CLICK_AREA_PRT_CODE=S05&ACTION_AF_CLICK=V1"><span class="cur_status none">현재 선택된 메뉴-</span><span class="menu_bg menu05">멜론TV</span></a>
						<div class="lay_menu">
							<ul>
								<li class="first_child"><a href="http://www.melon.com/tv/index.htm"><span class="menu_tv m1">오늘은 뭘 볼까</span></a></li>
								<li class=""><a href="http://www.melon.com/tv/mv/index.htm"><span class="menu_tv m2">뮤직비디오</span></a></li>
								<li class=""><a href="http://www.melon.com/tv/menu/index.htm?menuSeq=1"><span class="menu_tv m3">멜론 오리지널</span></a></li>
								<li class=""><a href="http://www.melon.com/tv/menu/index.htm?menuSeq=4"><span class="menu_tv m4">아티스트 업데이트</span></a></li>
								<li class=""><a href="http://www.melon.com/tv/menu/index.htm?menuSeq=3"><span class="menu_tv m5">방송</span></a></li>
							</ul>
						</div>
					</li>
					<li class="nth6">
						
						<a href="http://www.melon.com/artistplus/todayupdate/index.htm" class="cur_menu mlog" data="LOG_PRT_CODE=1&MENU_PRT_CODE=0&MENU_ID_LV1=&CLICK_AREA_PRT_CODE=S07&ACTION_AF_CLICK=V1"><span class="cur_status none">현재 선택된 메뉴-</span><span class="menu_bg menu06">스타포스트</span></a>
						<div class="lay_menu">
							<ul>
								<li class="first_child"><a href="http://www.melon.com/artistplus/todayupdate/index.htm"><span class="menu_arti m1">NOW</span></a></li>
								<li class=""><a href="http://www.melon.com/artistplus/themespecial/index.htm"><span class="menu_arti m2">테마스페셜</span></a></li>
								<li class=""><a href="http://www.melon.com/artistplus/artistchart/index.htm"><span class="menu_arti m3">아티스트 랭킹</span></a></li>
								<li class=""><a href="http://www.melon.com/artistplus/myranking/index.htm"><span class="menu_arti m4">마이 랭킹</span></a></li>
							</ul>						
							<div class="menu_artist_btn">
	                            <div class="artist_fan">
	                                <button type="button" class="btn_fan" onclick="MELON.WEBSVC.POC.menu.goMyMusicFanSignArtist();"><span class="odd_span">팬맺은 아티스트</span></button>
	                            </div>
	                            <div class="artist_finder">
	                                <button type="button" class="btn_artist_f" onclick="location.href='http://www.melon.com/artistplus/finder/index.htm'"><span class="odd_span">아티스트 파인더</span></button>
	                            </div>
							</div>
						</div>
					</li>
					<!-- 160314 수정 -->
					<li class="nth7">
						
						<a href="http://www.melon.com/musicstory/today/index.htm" class="cur_menu mlog" data="LOG_PRT_CODE=1&MENU_PRT_CODE=0&MENU_ID_LV1=&CLICK_AREA_PRT_CODE=S09&ACTION_AF_CLICK=V1"><span class="cur_status none">현재 선택된 메뉴-</span><span class="menu_bg menu07">멜론매거진</span></a>
					</li>
					<!-- // 160314 수정 -->
					<li class="nth8">
						
						<a href="http://www.melon.com/melonaward/timeline.htm" class="cur_menu mlog" data="LOG_PRT_CODE=1&MENU_PRT_CODE=0&MENU_ID_LV1=&CLICK_AREA_PRT_CODE=S11&ACTION_AF_CLICK=V1"><span class="cur_status none">현재 선택된 메뉴-</span><span class="menu_bg menu08">뮤직어워드</span></a>
					</li>
					
					<!-- 170531 수정 kjh -->
					<li class="nth10">
						
						<a href="http://www.melon.com/flac/index.htm" data="LOG_PRT_CODE=1&MENU_PRT_CODE=0&MENU_ID_LV1=&CLICK_AREA_PRT_CODE=C05&ACTION_AF_CLICK=V1" class="cur_menu mlog"><span class="cur_status none">현재 선택된 메뉴-</span><span class="menu_bg menu12">멜론Hi-Fi</span><span class="icon_new"></span></a>
					</li>
					<!-- //170531 수정 kjh -->
					
					
					<li class="nth9 last_child">
					<!-- //140523_수정 -->
						
						<a href="#" class="cur_menu mlog_without_page_change" data="LOG_PRT_CODE=1&MENU_PRT_CODE=0&MENU_ID_LV1=&CLICK_AREA_PRT_CODE=S99&ACTION_AF_CLICK=V1"><span class="cur_status none">현재 선택된 메뉴-</span><span class="menu_bg menu09">더보기</span></a>
						<div class="more_wrap" style="display:none"><!-- more_lay일때 display:block -->
							<ul>
								
								<li class="first_child"><a href="http://www.melon.com/smartradio/index.htm" class="mlog" data="LOG_PRT_CODE=1&MENU_PRT_CODE=0&MENU_ID_LV1=&CLICK_AREA_PRT_CODE=S06&ACTION_AF_CLICK=V1"><span class="menu_more m1">스마트라디오</span></a></li>
								
								<li class=""><a href="http://www.melon.com/edu/index.htm" class="mlog" data="LOG_PRT_CODE=1&MENU_PRT_CODE=0&MENU_ID_LV1=&CLICK_AREA_PRT_CODE=C04&ACTION_AF_CLICK=V1"><span class="menu_more m3">어학</span></a></li>
								
								<li class=""><a href="http://www.melon.com/customer/announce/index.htm" class="mlog" data="LOG_PRT_CODE=1&MENU_PRT_CODE=0&MENU_ID_LV1=&CLICK_AREA_PRT_CODE=V02&ACTION_AF_CLICK=V1"><span class="menu_more m4">공지사항</span></a></li>
							</ul>
						</div>

					</li>
				</ul>
				<ul class="sub_gnb">
					<li class="">
						
						<a href="javascript:MELON.WEBSVC.POC.menu.goMyMusicMain();" class="cur_menu mlog" data="LOG_PRT_CODE=1&MENU_PRT_CODE=0&MENU_ID_LV1=&CLICK_AREA_PRT_CODE=S01&ACTION_AF_CLICK=V1"><span class="cur_status none">현재 선택된 메뉴-</span><span class="menu_bg menu10">마이뮤직</span></a>
					</li>
					<li>
						
						<a href="javascript:MELON.WEBSVC.POC.menu.goFeed();" class="cur_menu mlog" data="LOG_PRT_CODE=1&MENU_PRT_CODE=0&MENU_ID_LV1=&CLICK_AREA_PRT_CODE=S02&ACTION_AF_CLICK=V1"><span class="cur_status none">현재 선택된 메뉴-</span><span class="menu_bg menu11">피드</span><span class="msg_box" style="display: none;"><span class="num">99+</span><span class="none">개</span></span></a>
					</li>
				</ul>
			</div>
			<!-- location 기획 요청으로 제거 2014-04-01 -->

			<!-- //location -->
		</div>
	</div>
	<!-- //header -->

	<div id="cont_wrap" class="clfix">
		<div id="conts_section" class="my_fold">
			<!-- contents -->
			


<!-- contents -->
				<div id="conts">
					<div class="page_header">
						<h2 class="title">멜론 TOP100</h2>
						<div class="tooltip">
							<button type="button" class="button_icons etc tooltip" data-control="dropdown"><span class="none">툴팁보기</span></button>
							<div class="layer_popup" role="dialog">
								<p class="desc">매시간 서비스 이용량 중 스트리밍 40%+다운로드 60%를 반영한 차트입니다.</p>
								<button type="button" class="button_icons etc close d_close"><span class="none">닫기</span></button>
							</div>
						</div>
					</div>
					<div class="wrap_tabmenu01">
						<ul>
							<li class="first_child on"><a href="/chart/index.htm"  class="link_tab"><span class="cntt">실시간</span></a></li>
							<li><a href="/chart/rise/index.htm"  class="link_tab" title="급상승 차트 - 페이지 이동"><span class="cntt">급상승</span></a></li>
							<li><a href="/chart/day/index.htm"  class="link_tab" title="일간 차트 - 페이지 이동"><span class="cntt">일간</span></a></li>
							<li><a href="/chart/week/index.htm"  class="link_tab" title="주간 차트 - 페이지 이동"><span class="cntt">주간</span></a></li>
							<li class="last_child"><a href="/chart/month/index.htm"  class="link_tab" title="월간 차트 - 페이지 이동"><span class="cntt">월간</span></a></li>
						</ul>
					</div>
					<div id="real_conts">
					


<div class="multi_row">
	<div class="calendar_prid">
		<span class="yyyymmdd">
			<span class="year">2018.01.25</span>
		</span>
		<span class="hhmm">
			<span class="hour">10:00</span>
		</span>
		<div class="time_layer">
			<button title="시간선택" class="button_icons etc arrow_d" type="button" data-control="dropdown">
				<span class="none">시간선택</span>
			</button>
			<div class="l_popup" style="display: none;">
				<div class="box_scroll">
					<ul class="time_list">
						
						
							
							
							
							
								
							
						
							
							
							
							
								
							
						
							
							
							
							
								
							
						
							
							
							
							
								
							
						
							
							
							
							
								
							
						
							
							
							
							
								
							
						
							
							
							
							
								
							
						
							
							
							
							
								
							
						
							
							
							
							
								
							
						
							
							
							
							
								
							
						
							
							
							
							
								
							
						
							
							
							
							
								
							
						
							
							
							
							
								
							
						
							
							
							
							
								
									<li><a href="#" class="timelist" data-time-value="2018012510"><span class="time">10:00</span></a></li>
								
							
						
							
							
							
								
							
							
								
									<li><a href="#" class="timelist" data-time-value="2018012509"><span class="time">09:00</span></a></li>
								
							
						
							
							
							
								
							
							
								
									<li><a href="#" class="timelist" data-time-value="2018012508"><span class="time">08:00</span></a></li>
								
							
						
							
							
							
								
							
							
								
									<li><a href="#" class="timelist" data-time-value="2018012507"><span class="time">07:00</span></a></li>
								
							
						
							
							
							
								
							
							
								
									<li><a href="#" class="timelist" data-time-value="2018012506"><span class="time">06:00</span></a></li>
								
							
						
							
							
							
								
							
							
								
									<li><a href="#" class="timelist" data-time-value="2018012505"><span class="time">05:00</span></a></li>
								
							
						
							
							
							
								
							
							
								
									<li><a href="#" class="timelist" data-time-value="2018012504"><span class="time">04:00</span></a></li>
								
							
						
							
							
							
								
							
							
								
									<li><a href="#" class="timelist" data-time-value="2018012503"><span class="time">03:00</span></a></li>
								
							
						
							
							
							
								
							
							
								
									<li><a href="#" class="timelist" data-time-value="2018012502"><span class="time">02:00</span></a></li>
								
							
						
							
							
							
								
							
							
								
									<li><a href="#" class="timelist" data-time-value="2018012501"><span class="time">01:00</span></a></li>
								
							
						
							
							
							
								
							
							
								
									<li><a href="#" class="timelist" data-time-value="2018012500"><span class="time">00:00</span></a></li>
								
							
						
					</ul>
				</div>
			</div>
			<span class="rank_update" style="display: none">순위 업데이트!</span>
		</div>
	</div>
	<div class="top3 button_group">
		<button type="button" id="d_tutorial_open" class="btn_guide"><span class="text">이용안내</span><span class="button_icons etc guide"></span></button>
		<button type="button" id="chart_Refresh"><span class="text btn_chart">새로고침</span><span class="button_icons etc refresh"></span></button>
	</div>
</div>
<div class="wrap_top3">
	<h3 class="none">실시간 TOP100 1위부터 3위까지 순위 목록</h3>
	<div class="real_graph">
		<div class="real_wrap">
			<div class="graph_bar">
				<a href="#" class="btn_five">5분보기</a>
			</div>
			<div class="graph_wrap">
				<span class="rank_txt">5분 차트보기</em></span>
				<div class="occupancy_cont">
					<div class="rank_time">
						<span class="time"> <img width="101" height="13" src="http://cdnimg.melon.co.kr/resource/image/web/chart/stit_realtime02.png" alt="실시간 점유율"/>
						</span>
						<ul>
							
								
									<li class="lank01"><a href="#"><span class="none">1위</span>
								
								
								<em>40%</em>
								</a></li>
							
								
								
									<li class="lank02"><a href="#"><span>2위</span>
								
								<em>30%</em>
								</a></li>
							
								
								
									<li class="lank03"><a href="#"><span>3위</span>
								
								<em>30%</em>
								</a></li>
							
						</ul>
					</div>
				</div>
				<div id="d_chart_box" class="graph_rank">
					<!-- 실시간 차트 랜더링 -->
				</div>
			</div>
			<div class="rank_cont d_songrankcont">
				<ol class="d_song_list">

					
						<li class="on">
							<div class="album_img">
								<img onerror="WEBPOCIMG.defaultAlbumImg(this);" width="319" height="319" src="http://cdnimg.melon.co.kr/cm/album/images/101/15/186/10115186_500.jpg/melon/resize/319/quality/80/optimize" alt="그날처럼 - 페이지 이동"/>
							</div>
							<div class="rank_music">
								<div class="music_info">
									<div class="info_top">
										<div class="chart_num">
											<span class="rank_01">1</span>
											<span class="none">위</span>
										</div>
										<div class="song_info_cont">
											<div class="thumb">
												<a href="javascript:melon.link.goAlbumDetail('10115186');"><img onerror="WEBPOCIMG.defaultAlbumImg(this);" width="80" height="80" src="http://cdnimg.melon.co.kr/cm/album/images/101/15/186/10115186_500.jpg/melon/resize/80/quality/80/optimize" alt="그날처럼 - 페이지 이동"/></a>
											</div>
											<div class="song_info_cont2">
												<div class="wrap_song_info ellipsis">
													
													<strong>
														<a title="그날처럼 - 재생" href="javascript:melon.play.playSong('19030101','30755375');">
															<span class="ellipsis">
																<span class="play">재생</span>
															
															
															
																<span class="tit">그날처럼</span>
															</span>
														</a>
													</strong>
													
													
												</div>
												<div class="wrap_atist"><a href="javascript:melon.link.goArtistDetail('829211');" title="장덕철 - 페이지 이동" class="play_artist"><span>장덕철</span></a></div>
												<div class="btn_like" >
													<button class="btn_icon like"
														title="그날처럼 좋아요"
														type="button" data-song-no="30755375"
														data-song-menuId="19030101" style="display:none;">
														<span class="odd_span">좋아요</span> <span class="cnt"><span
															class="none">총건수</span>0</span>
													</button>
												</div>
											</div>
										</div>
									</div>
									<div class="info_btm">
										<div class="info_btm">
											<ul>
												
												
													<li><span class="icon_info issue"></span><em class="inssue_txt">이슈</em>1위지속 <em><span>23</span>시간 이상 1위!!</em></li>
												
												<li><span class="icon_info max"></span>24시간 내 최고 순위 <em>1위</em></li>
												
												
												
												
												
												<li><span class="icon_info dauily"></span>어제 누적 순위 <em>2위</em></li>
												
											</ul>
										</div>
									</div>
									
										<a href="#" class="btn_hearing" title="1위곡 누가 들었나요?">
										<img src="http://cdnimg.melon.co.kr/resource/image/web/chart_4x/btn_rank.png" alt="1위곡 누가 들었나요?"/></a>
									
								</div>
							</div>
							
								<div class="hearing_layer">
									<div class="wrap">
										<div class="cont">
											<h3>
												<span class="rank_01">1</span>
											</h3>
											<p class="txt_desc"><img src="http://cdnimg.melon.co.kr/resource/image/web/chart/txt_vote.gif" alt="누가 들었나요?최근 24시간 동안 스트리밍과 다운로드를 한 감상 이용자 정보입니다."/></p>
											<ul>
												<li class="lank01"><a href="#"><span class="none">1위</span><em>40%</em></a></li>
												<li class="lank02"><a href="#"><span class="none">2위</span><em>30%</em></a></li>
												<li class="lank03"><a href="#"><span class="none">3위</span><em>30%</em></a></li>
											</ul>
											
											
											
											
											
											
											
											
											
											<ul class="gender">
												<li style="width:51.1%;" class="man"><strong><span>남자</span></strong>
													<span class="graph_bar2"><span><em>51.1%</em></span></span>
												</li>
												<li style="width:48.9%;" class="woman"><strong><span>여자</span></strong>
													<span class="graph_bar2"><span><em>48.9%</em></span></span>
												</li>
											</ul>
											<ul class="age_group">
												<li class="nth1"><strong><span>10대</span></strong> <span
													class="graph_bar2"><span style="height:11.9%"></span></span>
												</li>
												<li class="nth2"><strong><span>20대</span></strong> <span
													class="graph_bar2"><span style="height:50.9%"></span></span>
												</li>
												<li class="nth3"><strong><span>30대</span></strong> <span
													class="graph_bar2"><span style="height:19.8%"></span></span>
												</li>
												<li class="nth4"><strong><span>40대</span></strong> <span
													class="graph_bar2"><span style="height:11.7%"></span></span>
												</li>
												<li class="nth5"><strong><span>50대</span></strong> <span
													class="graph_bar2"><span style="height:4.6%"></span></span>
												</li>
												<li class="nth6"><strong><span>기타</span></strong> <span
													class="graph_bar2"><span style="height:1.1%"></span></span>
												</li>
											</ul>
											<div class="count_num">
												<strong class="count">이용자수</strong> <em>688,859</em>
												<span class="unit">명</span>
												<span class="hour">(24시간 누적)</span>
											</div>
										</div>
										<button type="button" class="btn d_close">닫기</button>
									</div>
								</div>
							
						</li>
					
						<li >
							<div class="album_img">
								<img onerror="WEBPOCIMG.defaultAlbumImg(this);" width="319" height="319" src="http://cdnimg.melon.co.kr/cm/album/images/101/31/396/10131396_500.jpg/melon/resize/319/quality/80/optimize" alt="다른사람을 사랑하고 있어 - 페이지 이동"/>
							</div>
							<div class="rank_music">
								<div class="music_info">
									<div class="info_top">
										<div class="chart_num">
											<span class="rank_02">2</span>
											<span class="none">위</span>
										</div>
										<div class="song_info_cont">
											<div class="thumb">
												<a href="javascript:melon.link.goAlbumDetail('10131396');"><img onerror="WEBPOCIMG.defaultAlbumImg(this);" width="80" height="80" src="http://cdnimg.melon.co.kr/cm/album/images/101/31/396/10131396_500.jpg/melon/resize/80/quality/80/optimize" alt="다른사람을 사랑하고 있어 - 페이지 이동"/></a>
											</div>
											<div class="song_info_cont2">
												<div class="wrap_song_info ellipsis">
													
													<strong>
														<a title="다른사람을 사랑하고 있어 - 재생" href="javascript:melon.play.playSong('19030101','30851703');">
															<span class="ellipsis">
																<span class="play">재생</span>
															
															
															
																<span class="tit">다른사람을 사랑하고 있어</span>
															</span>
														</a>
													</strong>
													
													
												</div>
												<div class="wrap_atist"><a href="javascript:melon.link.goArtistDetail('514741');" title="수지 (SUZY) - 페이지 이동" class="play_artist"><span>수지 (SUZY)</span></a></div>
												<div class="btn_like" >
													<button class="btn_icon like"
														title="다른사람을 사랑하고 있어 좋아요"
														type="button" data-song-no="30851703"
														data-song-menuId="19030101" style="display:none;">
														<span class="odd_span">좋아요</span> <span class="cnt"><span
															class="none">총건수</span>0</span>
													</button>
												</div>
											</div>
										</div>
									</div>
									<div class="info_btm">
										<div class="info_btm">
											<ul>
												
												
												<li><span class="icon_info max"></span>24시간 내 최고 순위 <em>2위</em></li>
												
												
												
												
												
												<li><span class="icon_info dauily"></span>어제 누적 순위 <em>1위</em></li>
												
											</ul>
										</div>
									</div>
									
										<a href="#" class="btn_hearing" title="2위곡 누가 들었나요?">
										<img src="http://cdnimg.melon.co.kr/resource/image/web/chart_4x/btn_rank.png" alt="2위곡 누가 들었나요?"/></a>
									
								</div>
							</div>
							
								<div class="hearing_layer">
									<div class="wrap">
										<div class="cont">
											<h3>
												<span class="rank_02">2</span>
											</h3>
											<p class="txt_desc"><img src="http://cdnimg.melon.co.kr/resource/image/web/chart/txt_vote.gif" alt="누가 들었나요?최근 24시간 동안 스트리밍과 다운로드를 한 감상 이용자 정보입니다."/></p>
											<ul>
												<li class="lank01"><a href="#"><span class="none">1위</span><em>40%</em></a></li>
												<li class="lank02"><a href="#"><span class="none">2위</span><em>30%</em></a></li>
												<li class="lank03"><a href="#"><span class="none">3위</span><em>30%</em></a></li>
											</ul>
											
											
											
											
											
											
											
											
											
											<ul class="gender">
												<li style="width:40.5%;" class="man"><strong><span>남자</span></strong>
													<span class="graph_bar2"><span><em>40.5%</em></span></span>
												</li>
												<li style="width:59.5%;" class="woman"><strong><span>여자</span></strong>
													<span class="graph_bar2"><span><em>59.5%</em></span></span>
												</li>
											</ul>
											<ul class="age_group">
												<li class="nth1"><strong><span>10대</span></strong> <span
													class="graph_bar2"><span style="height:12.7%"></span></span>
												</li>
												<li class="nth2"><strong><span>20대</span></strong> <span
													class="graph_bar2"><span style="height:49.8%"></span></span>
												</li>
												<li class="nth3"><strong><span>30대</span></strong> <span
													class="graph_bar2"><span style="height:21.0%"></span></span>
												</li>
												<li class="nth4"><strong><span>40대</span></strong> <span
													class="graph_bar2"><span style="height:11.3%"></span></span>
												</li>
												<li class="nth5"><strong><span>50대</span></strong> <span
													class="graph_bar2"><span style="height:4.3%"></span></span>
												</li>
												<li class="nth6"><strong><span>기타</span></strong> <span
													class="graph_bar2"><span style="height:1.0%"></span></span>
												</li>
											</ul>
											<div class="count_num">
												<strong class="count">이용자수</strong> <em>538,271</em>
												<span class="unit">명</span>
												<span class="hour">(24시간 누적)</span>
											</div>
										</div>
										<button type="button" class="btn d_close">닫기</button>
									</div>
								</div>
							
						</li>
					
						<li >
							<div class="album_img">
								<img onerror="WEBPOCIMG.defaultAlbumImg(this);" width="319" height="319" src="http://cdnimg.melon.co.kr/cm/album/images/101/28/855/10128855_500.jpg/melon/resize/319/quality/80/optimize" alt="주인공 - 페이지 이동"/>
							</div>
							<div class="rank_music">
								<div class="music_info">
									<div class="info_top">
										<div class="chart_num">
											<span class="rank_03">3</span>
											<span class="none">위</span>
										</div>
										<div class="song_info_cont">
											<div class="thumb">
												<a href="javascript:melon.link.goAlbumDetail('10128855');"><img onerror="WEBPOCIMG.defaultAlbumImg(this);" width="80" height="80" src="http://cdnimg.melon.co.kr/cm/album/images/101/28/855/10128855_500.jpg/melon/resize/80/quality/80/optimize" alt="주인공 - 페이지 이동"/></a>
											</div>
											<div class="song_info_cont2">
												<div class="wrap_song_info ellipsis">
													
													<strong>
														<a title="주인공 - 재생" href="javascript:melon.play.playSong('19030101','30838076');">
															<span class="ellipsis">
																<span class="play">재생</span>
															
															
															
																<span class="tit">주인공</span>
															</span>
														</a>
													</strong>
													
													
												</div>
												<div class="wrap_atist"><a href="javascript:melon.link.goArtistDetail('22938');" title="선미 - 페이지 이동" class="play_artist"><span>선미</span></a></div>
												<div class="btn_like" >
													<button class="btn_icon like"
														title="주인공 좋아요"
														type="button" data-song-no="30838076"
														data-song-menuId="19030101" style="display:none;">
														<span class="odd_span">좋아요</span> <span class="cnt"><span
															class="none">총건수</span>0</span>
													</button>
												</div>
											</div>
										</div>
									</div>
									<div class="info_btm">
										<div class="info_btm">
											<ul>
												
												
												<li><span class="icon_info max"></span>24시간 내 최고 순위 <em>2위</em></li>
												
												
												
												
												
												<li><span class="icon_info dauily"></span>어제 누적 순위 <em>3위</em></li>
												
											</ul>
										</div>
									</div>
									
										<a href="#" class="btn_hearing" title="3위곡 누가 들었나요?">
										<img src="http://cdnimg.melon.co.kr/resource/image/web/chart_4x/btn_rank.png" alt="3위곡 누가 들었나요?"/></a>
									
								</div>
							</div>
							
								<div class="hearing_layer">
									<div class="wrap">
										<div class="cont">
											<h3>
												<span class="rank_03">3</span>
											</h3>
											<p class="txt_desc"><img src="http://cdnimg.melon.co.kr/resource/image/web/chart/txt_vote.gif" alt="누가 들었나요?최근 24시간 동안 스트리밍과 다운로드를 한 감상 이용자 정보입니다."/></p>
											<ul>
												<li class="lank01"><a href="#"><span class="none">1위</span><em>40%</em></a></li>
												<li class="lank02"><a href="#"><span class="none">2위</span><em>30%</em></a></li>
												<li class="lank03"><a href="#"><span class="none">3위</span><em>30%</em></a></li>
											</ul>
											
											
											
											
											
											
											
											
											
											<ul class="gender">
												<li style="width:41.4%;" class="man"><strong><span>남자</span></strong>
													<span class="graph_bar2"><span><em>41.4%</em></span></span>
												</li>
												<li style="width:58.6%;" class="woman"><strong><span>여자</span></strong>
													<span class="graph_bar2"><span><em>58.6%</em></span></span>
												</li>
											</ul>
											<ul class="age_group">
												<li class="nth1"><strong><span>10대</span></strong> <span
													class="graph_bar2"><span style="height:12.3%"></span></span>
												</li>
												<li class="nth2"><strong><span>20대</span></strong> <span
													class="graph_bar2"><span style="height:49.0%"></span></span>
												</li>
												<li class="nth3"><strong><span>30대</span></strong> <span
													class="graph_bar2"><span style="height:21.3%"></span></span>
												</li>
												<li class="nth4"><strong><span>40대</span></strong> <span
													class="graph_bar2"><span style="height:12.0%"></span></span>
												</li>
												<li class="nth5"><strong><span>50대</span></strong> <span
													class="graph_bar2"><span style="height:4.4%"></span></span>
												</li>
												<li class="nth6"><strong><span>기타</span></strong> <span
													class="graph_bar2"><span style="height:1.1%"></span></span>
												</li>
											</ul>
											<div class="count_num">
												<strong class="count">이용자수</strong> <em>531,686</em>
												<span class="unit">명</span>
												<span class="hour">(24시간 누적)</span>
											</div>
										</div>
										<button type="button" class="btn d_close">닫기</button>
									</div>
								</div>
							
						</li>
					
				</ol>
			</div>
		</div>
		<!-- 5분단위 확장 -->
		<div class="five_wrap" style="display: none;">
			<div class="graph_wrap">
				<div class="occupancy_cont">
					<div class="rank_time">
						<span class="time">
							<img width="361" height="16" src="http://cdnimg.melon.co.kr/resource/image/web/chart/stit_five.png" alt="5분단위 점유율이 누적되어 다음 시간의 순위가 결정됩니다."/>
						</span>
					</div>
				</div>
				<div id="d_chart_box2" class="graph_rank">
					<!-- 5분차트 랜더링 -->
				</div>
			</div>
			<div class="graph_bar mactive">
				<a href="#" class="btn_five">5분보기</a>
			</div>
			<div class="five_graph">
				<div class="d_songrankcont">
					<div id="d_ranktimer" class="time_five">
						<div class="txt_five"><span class="none">현재기준</span><em>11:00</em><span class="none"> 순위예측</span></div>
						<div class="real_time">
							<span class="time1">
								<span>1</span><span>7</span>
							</span> :
							<span class="time2">
								<span>5</span><span>5</span>
							</span> :
							<span class="time3">
								<span>3</span><span>9</span>
							</span>
						</div>
					</div>
					<ol class="d_song_list">
						
							<li id="series30755375">
								<div class="album_img">
									<img onerror="WEBPOCIMG.defaultAlbumImg(this);" width="319" height="319" src="http://cdnimg.melon.co.kr/cm/album/images/101/15/186/10115186_500.jpg/melon/resize/319/quality/80/optimize" alt="그날처럼 - 페이지 이동"/>
								</div>
								<div class="rank_music">
									<div class="music_info">
										<div class="info_top">
											<div class="chart_num">
												<span class="d_rank_tmp">{rank}</span>
												<span class="none">위 예측</span>
											</div>
											<div class="wrap_song_info ellipsis">
												<span>
												
												
												
													<strong>
													<a title="그날처럼 재생" href="javascript:melon.play.playSong('19030101','30755375');" class="btn_play_song">
														<span class="play">재생</span>
														<span class="tit">그날처럼</span>
													</a>
													</strong>
												
												</span>
											</div>
											<div class="wrap_atist"><a href="javascript:melon.link.goArtistDetail('829211');" title="장덕철 - 페이지 이동" class="play_artist"><span>장덕철</span></a></div>
											<div class="btn_like" >
												<button class="btn_icon like" title="그날처럼 좋아요" type="button" data-song-no="30755375" data-song-menuId="19030101" style="display:none;">
													<span class="odd_span">좋아요</span>
													<span class="cnt"><span class="none">총건수</span>0</span>
												</button>
											</div>
										</div>
									</div>
								</div>
							</li>
						
							<li id="series30838076">
								<div class="album_img">
									<img onerror="WEBPOCIMG.defaultAlbumImg(this);" width="319" height="319" src="http://cdnimg.melon.co.kr/cm/album/images/101/28/855/10128855_500.jpg/melon/resize/319/quality/80/optimize" alt="주인공 - 페이지 이동"/>
								</div>
								<div class="rank_music">
									<div class="music_info">
										<div class="info_top">
											<div class="chart_num">
												<span class="d_rank_tmp">{rank}</span>
												<span class="none">위 예측</span>
											</div>
											<div class="wrap_song_info ellipsis">
												<span>
												
												
												
													<strong>
													<a title="주인공 재생" href="javascript:melon.play.playSong('19030101','30838076');" class="btn_play_song">
														<span class="play">재생</span>
														<span class="tit">주인공</span>
													</a>
													</strong>
												
												</span>
											</div>
											<div class="wrap_atist"><a href="javascript:melon.link.goArtistDetail('22938');" title="선미 - 페이지 이동" class="play_artist"><span>선미</span></a></div>
											<div class="btn_like" >
												<button class="btn_icon like" title="주인공 좋아요" type="button" data-song-no="30838076" data-song-menuId="19030101" style="display:none;">
													<span class="odd_span">좋아요</span>
													<span class="cnt"><span class="none">총건수</span>0</span>
												</button>
											</div>
										</div>
									</div>
								</div>
							</li>
						
							<li id="series30851703">
								<div class="album_img">
									<img onerror="WEBPOCIMG.defaultAlbumImg(this);" width="319" height="319" src="http://cdnimg.melon.co.kr/cm/album/images/101/31/396/10131396_500.jpg/melon/resize/319/quality/80/optimize" alt="다른사람을 사랑하고 있어 - 페이지 이동"/>
								</div>
								<div class="rank_music">
									<div class="music_info">
										<div class="info_top">
											<div class="chart_num">
												<span class="d_rank_tmp">{rank}</span>
												<span class="none">위 예측</span>
											</div>
											<div class="wrap_song_info ellipsis">
												<span>
												
												
												
													<strong>
													<a title="다른사람을 사랑하고 있어 재생" href="javascript:melon.play.playSong('19030101','30851703');" class="btn_play_song">
														<span class="play">재생</span>
														<span class="tit">다른사람을 사랑하고 있어</span>
													</a>
													</strong>
												
												</span>
											</div>
											<div class="wrap_atist"><a href="javascript:melon.link.goArtistDetail('514741');" title="수지 (SUZY) - 페이지 이동" class="play_artist"><span>수지 (SUZY)</span></a></div>
											<div class="btn_like" >
												<button class="btn_icon like" title="다른사람을 사랑하고 있어 좋아요" type="button" data-song-no="30851703" data-song-menuId="19030101" style="display:none;">
													<span class="odd_span">좋아요</span>
													<span class="cnt"><span class="none">총건수</span>0</span>
												</button>
											</div>
										</div>
									</div>
								</div>
							</li>
						
					</ol>
				</div>
			</div>
		</div>
		<!-- //5분단위 확장 -->

		<!-- 경합중 레이어 -->
		<div id="d_chart_L" class="rank_layer" style="left: 198px; top: 60px; display: none;">
			<div class="wrap">
				<span class="num_01">
					<span class="thumb">
						<span class="thumb_frame"></span>
						<img onerror="WEBPOCIMG.defaultAlbumImg(this);" width="85" height="85" src="http://cdnimg.melon.co.kr/cm/album/images/101/15/186/10115186_500.jpg/melon/resize/85/quality/80/optimize" alt=""/>
					</span>
				</span>
				<span class="none">1 VS 2 경합중!</span>
				<span class="num_02">
					<span class="thumb">
						<span class="thumb_frame"></span>
						<img onerror="WEBPOCIMG.defaultAlbumImg(this);" width="85" height="85" src="http://cdnimg.melon.co.kr/cm/album/images/101/31/396/10131396_500.jpg/melon/resize/85/quality/80/optimize" alt=""/>
					</span>
				</span>
				<button type="button" class="btn d_close">닫기</button>
			</div>
		</div>

		<!-- 차트올킬 레이어 -->
		<div id="d_chart_L2" class="rank_layer" style="left: 271px; top: 60px; display: none;">
			<div class="wrap all_kill">
				<span class="num_123">
					<span class="thumb">
						<span class="thumb_frame"></span>
						<img width="128" height="128" src="http://cdnimg.melon.co.kr/cm/album/images/101/15/186/10115186_500.jpg/melon/resize/128/quality/80/optimize" alt=""/>
					</span>
				</span>
				<span class="none">1/2/3 차트 올~킬!!</span>
				<button type="button" class="btn d_close">닫기</button>
			</div>
		</div>
	</div>
</div>
<!-- //TOP3 -->
<div id="tutorial" class="tutorial_wrap" style="display: none">
	<div class="tutorial">
		<img usemap="#urlLink" src="http://cdnimg.melon.co.kr/resource/image/web/chart_4x/img_tutorial01_20170913.png" alt=""/>
		<map id="urlLink" name="urlLink">
			<area class="d_close" shape="rect" coords="956,24,981,49" href="#" alt="닫기" />
		</map>
	</div>
	<ul class="tab">
		<li class="on"><a href="#"><img src="http://cdnimg.melon.co.kr/resource/image/web/chart_4x/tab_tutorial01.png" alt="1.더 다양한 차트"/></a></li>
		<li><a href="#"><img src="http://cdnimg.melon.co.kr/resource/image/web/chart_4x/tab_tutorial02.png" alt="2.더 정확한 차트"/></a></li>
		<li><a href="#"><img src="http://cdnimg.melon.co.kr/resource/image/web/chart_4x/tab_tutorial03.png" alt="3.더 재미있는 차트"/></a></li>
	</ul>
	<div class="btn_next">
		<a href="#"><img src="http://cdnimg.melon.co.kr/resource/image/web/chart/btn_next.png" alt="다음"/></a>
	</div>
</div>
<script type="text/javascript" src="/resource/script/web/chart/json2.js"></script>
<script type="text/javascript">
var bigV = '';
var rankStyle = {
	color : ['#a7e52e', '#f6894e', '#59afe5', '#fd7db9', '#c998ff', '#39c5c2'],
	marker : [5, 5, 5],
	symbol : ['circle', 'square', 'diamond']
};
var chartCommSet = {
	credits: { enabled: false },
	title: { text: '' },
	legend: { enabled: false}
};

var chartExp;
var seriesRankingState = [];
var mouseMoveTimerId;
var seriesCommSet = {
		events:{
			mouseOver:function(e){
				var index = this.index;
				if($(this.chart.renderTo).is('#d_chart_box2')){
					clearTimeout(mouseMoveTimerId);
					if(seriesRankingState[index] < 4){
						chartExp.change(index);
						if(seriesRankingState[index] == series.length){
							chartExp.prevIdx = 2
						}else{
							chartExp.prevIdx = seriesRankingState[index]-1;
						}
					}
				}
			}
		}
};
var series =
	[{ type : "line", index: 0, name : "그날처럼", data: [4.399,3.869,3.838,3.861,3.853,3.845,3.972,4.159,4.356,4.063,3.946,4.063,4.234,4.258,4.097,3.813,3.489,3.178,2.908,2.888,3.725,5.047,5.191,4.955]},
	 { type : "line", index: 1, name : "다른사람을 사랑하고 있어", data: [3.691,3.187,3.165,3.177,3.038,2.953,2.814,2.910,3.201,2.912,2.866,3.000,3.114,3.213,3.273,2.919,2.509,2.131,1.797,1.698,2.293,4.052,4.446,3.959]},
	 { type : "line", index: 2, name : "주인공", data: [3.472,3.043,2.996,3.065,2.998,2.982,3.183,3.324,3.587,3.300,3.185,3.274,3.283,3.148,2.751,2.423,2.101,1.740,1.509,1.484,2.166,3.730,4.311,3.891]}];

var rankSeries =
	[{data : [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]},
	 {data : [2,2,2,2,2,3,3,3,3,3,3,3,3,2,2,2,2,3,6,10,3,2,2,2]},
	 {data : [3,3,3,3,3,2,2,2,2,2,2,2,2,3,3,3,4,8,14,15,4,3,3,3]}];

var fiveSeries = [];
var fiveData;

	fiveSeries.push(
		{
			type : "line",
			name:  "30755375",
			data: ['', 4.95463,4.72602,4.60887,4.60484,4.61678,4.605,4.57449,4.56739,4.53913]
		}
	);
	fiveData = fiveSeries[0].data;

	fiveSeries.push(
		{
			type : "line",
			name:  "30851703",
			data: ['', 3.95866,3.81486,3.69584,3.68278,3.67396,3.64967,3.6235,3.5878,3.55356]
		}
	);
	fiveData = fiveSeries[1].data;

	fiveSeries.push(
		{
			type : "line",
			name:  "30838076",
			data: ['', 3.89058,3.48661,3.49169,3.55177,3.56779,3.59027,3.59166,3.58821,3.57519]
		}
	);
	fiveData = fiveSeries[2].data;


var errMarker = {
	errsector : [  ],
	fiveErrsector : [],
	init : function(_series, type){
		var me = this;
		me.seriesType = type;
		me._series = JSON.parse(JSON.stringify(_series));
		me.secCheck();
	},
	secCheck : function(){
		var me = this,
			_seriesData;
			tmpArr = 0,
			sectorIdx = 0,
			errchk = false,
			_Val = [];

		if(me.seriesType == "real"){
			for (var t = 0,tlen = me._series.length; t < tlen; t++){
				_seriesData = me._series[t].data;
				sectorIdx = 0;
				for (var i = 0; i < me.errsector.length; i++) {
					var start = me.errsector[i][0] -1,
						last = me.errsector[i][1] +1;

					if (start == -1) {
						start = 0;
					};

					_Val.push(_seriesData[start],_seriesData[last]);
					me.lineAnker(t, _Val, sectorIdx);
					_Val = [];
					sectorIdx++;
				};
			};
		}else {
			for (var t = 0,tlen = me._series.length; t < tlen; t++){
				 _seriesData = me._series[t].data;
				sectorIdx = 0;
				for (var i = 0,len = _seriesData.length; i < len; i++){
					if(errchk && _seriesData[i] != 0){
						_Val.push(_seriesData[i]);
						me.lineAnker(t, _Val, sectorIdx);
						_Val = [];
						errchk = false;
						tmpArr = null;
						sectorIdx++;
					}
					if(_seriesData[i] == 0){
						var otherLen = 0;
						for (var k = 0,klen = me._series.length; k < klen; k++){
							_otherSeriesData = me._series[k].data;
							if (_otherSeriesData[i] == 0) {
								otherLen++;
							};
						};
						if (otherLen == me._series.length) {
							errchk = true;
							tmpArr = i;
							if(_seriesData[i-1] != 0){
								if(t < 1){
									me.fiveErrsector[sectorIdx] = [];
								}
								_Val.push((_seriesData[i-1]) ?  _seriesData[i-1] : 0)
							}
							if(t < 1){
								me.fiveErrsector[sectorIdx].push(tmpArr);
							}
						};
					}
				}
			}
		}
	},
	lineAnker : function(seriesIdx ,_val, idx){
		var me = this;
		if(me.seriesType == "real"){
			var gap = _val[0] - _val[1],
				sum = _val[0],
				reDateArr = [],
				len = me.errsector[idx][1] - me.errsector[idx][0] + 1;

				if(me.errsector[idx][0] == 0){
					reDateArr.push(0)
					gap = 0 - _val[1];
					sum = 0;
					gap = gap / len;
					for(var i=0; i < len-1 ; i++){
						sum -= gap;
						reDateArr.push(eval(sum.toString().substr(0, 5)));
					}
				}else{
					gap = gap / (len+1);
					for(var i=0; i < len ; i++){
						sum -= gap;
						reDateArr.push(eval(sum.toString().substr(0, 5)));
					}
				}
		}else {
			var gap = _val[0] - _val[1],
				sum = _val[0],
				reDateArr = [],
				len = me.fiveErrsector[idx].length;

				if(me.fiveErrsector[idx][0] == 0){
					reDateArr.push(0.2)
					gap = 0.2 - _val[1];
					sum = 0.2;
					gap = gap / len;
					for(var i=0; i < len-1 ; i++){
						sum -= gap;
						reDateArr.push(eval(sum.toString().substr(0, 5)));
					}
				}else{
					gap = gap / (len+1);
					for(var i=0; i < len ; i++){
						sum -= gap;
						reDateArr.push(eval(sum.toString().substr(0, 5)));
					}
				}
		}
		me.writeData(seriesIdx, reDateArr, idx)
	},
	writeData : function(seriesIdx, arr, idx){
		var me = this;
		if(me.seriesType == "real"){
			var len = me.errsector[idx][1] - me.errsector[idx][0] + 1;
			for(var t=0, tlen=len; t< tlen ; t++){
				var dataIdx = me.errsector[idx][0] + t;

			  series[seriesIdx].data[dataIdx] = {y: arr[t] ,marker :{ enabled:false}};
			}
		}else {
			for(var t=0, tlen=me.fiveErrsector[idx].length; t< tlen ; t++){
			  fiveSeries[seriesIdx].data[me.fiveErrsector[idx][t]] = {y: arr[t] ,marker :{ enabled:false}};
			}
		}
	}
};

var errfiveChart = true;
var errRealChart = false;
if (errRealChart){
	errMarker.init(series, 'real');
	series.errSector = errMarker.errsector;
}

var seriesSTATE = "";

if ( 'N' == 'Y' ) {
	seriesSTATE = "경합 중";
}
if ( 'N' == 'Y' ) {
	seriesSTATE = seriesSTATE + "차트 올킬";
}
var sevCount = 0;
var sevPoint;
for ( var i=0; i < series.length; i++ ) {
	dataArr = series[i].data;
	for ( var j=0; j < dataArr.length; j++ ) {
		if ( dataArr[j] >= 7 ) {
			sevCount++;
			sevPoint = j;
		}
	}
	if ( sevCount > 0 ) {
		series[i].data[sevPoint] = {pin: true, y: series[i].data[sevPoint] , marker : { symbol : "지붕킥 " + sevCount + "회"}};

	}
	sevCount = 0;
	sevPoint = 0;
}
var dapPoint;
for ( var i=0; i < series.length; i++ ) {
	dataArr = series[i].data;
	for ( var j=0; j < dataArr.length; j++ ) {
		if ( dataArr[j] >= 6 && dataArr[j] < 7 ) {
			if ( j > 0 && series[i].data[j] > series[i].data[j-1]) {
				series[i].data[j] = typeof series[i].data[j].y === 'undefined' ? series[i].data[j] : series[i].data[j].y;

				if ( j < dataArr.length - 1 && typeof series[i].data[j+1].y === 'undefined' ) {
					if ( series[i].data[j+1] < 7.0 ) {
					} else {
						series[i].data[j] = {pin: true, y: series[i].data[j] , marker : { symbol :"지붕킥 임박"}};
					}
				}
				if ( j == dataArr.length -1 ) {
					series[i].data[j] = {pin: true, y: series[i].data[j] , marker : { symbol :"지붕킥 임박"}};
				}
			}
		}
	}
}
var dataArr = rankSeries[0].data;
var topTick = "";
var topRank = 0;
for ( var j=0; j < dataArr.length; j++ ) {
	if ( dataArr[j] == 1) {
		if (topTick == "Y") {
			topRank++;
		} else {
			series[0].data[j] = typeof series[0].data[j].y === 'undefined' ? series[0].data[j] : series[0].data[j].y;
			if ( j > 0 ) {
				series[0].data[j] = {pin: true, y: series[0].data[j] ,  marker : { symbol : "1위 등극" }}; //140610_디자인적용
			}
			topTick = "Y";
			topRank++;
		}
	} else {
		topRank = 0;
	}
}
var arrSeries1 = series[0].data;
var arrSeries2 = series[1].data;
var arrSeries3 = series[2].data;
</script>
<script type="text/javascript">

$(function() {
	$('#chart_Refresh').click(function() {
		moveTime();
	});
	$('a.timelist').click(function() {
		moveTime($(this).attr("data-time-value"));
	});
	moveTime = function(t) {
		var pUrl = "?dayTime=" + t;
		if ( typeof t === 'undefined') { pUrl = ""; }
		document.location.href = "/chart/index.htm" + pUrl;
	}
});

$(function() {
	var WEBSVC = MELON.WEBSVC,
		PBPGN  = MELON.PBPGN;

	var logger = window.logger = Logger.get('Melon Core');
	logger.setLevel(Logger.DEBUG);

	(function(){
		var categories = ['11','12','13','14','15','16','17','18','19','20','21','22','23','00','01','02','03','04','05','06','07','08','09','10'],
			numberUtil = WEBSVC.number,
			len = series[0].data.length,
			categories2 = ['55','10:00','10:05','10:10','10:15','10:20','10:25','10:30','10:35','10:40','10:45','10:50','10:55']

			var chartsData = $.extend({
				chart: {
					marginTop: 10,
					marginRight: 42,
					marginLeft: 4,
					marginBottom:35,
					borderRadius : 0,
					backgroundColor : false,
					style : {
						overflow : 'visible',
						zIndex: 1
					}
				},
				xAxis: {
					max: 23,
					min: 0,
					categories: categories,
					labels: {
						useHTML : true,
						style : {
							color:"#a1adc6",
							fontSize:"11px"
						},
						format:'<span class="d_xlabel">{value}</span>'
						, y:18
					},
					lineWidth:0,
					tickWidth: 0,
					endOnTick: false,
					tickmarkPlacement: false,
					gridLineWidth: 0,
					gridLineColor: '#6f788b',
					gridLineDashStyle: 'solid'
				},
				yAxis: {
					title: {
						text: ''
					},
					min: 0.2,
					max: 7.04,
					labels: {
						enabled : false
					},
					visible: false,
					startOnTick: false,
					endOnTick: false,
					gridLine : false,
					gridLineWidth: 0
				},
				tooltip: {
					useHTML :true,
					headerFormat : '',
					style : {
						visibility: 'visible',
						color:"#000",
						fontSize:"11px"
					},
					formatter : function(){
						var cr = rankSeries[this.series.index].data[$.inArray(this.x, categories)];
						if (cr >= 100) {
							return false;
						} else {
							return '<span>시간: <b>'+this.x+ ":00</b> <br/> 순위 : <b>"+rankSeries[this.series.index].data[$.inArray(this.x, categories)]+'위</b></span>'
						}

					}
				},
				plotOptions: {
					series: {
						allowPointSelect: false,
						point: {
							events: {
								mouseOver: function() {
									if(this.series.userOptions.index != $('.rank_time ul li.on').index()){
										$('.highcharts-tooltip').hide();
									}else{
										$('.highcharts-tooltip').show();
									}
								}
							}
						},
						marker : {
							enabled : false,
							states : {
								hover : {
									enabled : false
								}
							}
						},
						states : {
							hover : {
								enabled : false
							}
						}
					}
				},
				series: series
			}, chartCommSet);

			var chartConfig = function(){
				var _labelVal = null, _labelTxt = null;

				for(var i=0; i<series.length; i++){
					$.extend(series[i], seriesCommSet);
				}
				for(var i=0; i<series.length; i++){
					series[i].color = rankStyle.color[i];
					for(var t=0; t < series[i].data.length ; t++){
						if(series[i].data[t].pin){
							_labelTxt = series[i].data[t].marker.symbol;
							if(_labelTxt.indexOf('지붕킥') != -1){
								if(_labelTxt.split('지붕킥 ')[1] == "임박"){
									_labelVal = "issue2_s"+(i+1);
								}else{
									_labelVal = "kick"+parseInt(_labelTxt.split('지붕킥 ')[1]);
								}
							}else{
								switch(_labelTxt){
									case "12시간 이상 1위":
										_labelVal = "issue1_s"+(i+1);
										break;
									case "1위 등극":
										_labelVal = "issue3_s"+(i+1);
										break;
								}
							}
							series[i].data[t].marker.symbol = 'url(http://image.melon.co.kr/resource/image/web/chart/icon_'+_labelVal+'.png)';
						}
					}
					series[i].marker = {
						radius : 3,
						symbol : rankStyle.symbol[0],
						lineColor: rankStyle.color[i],
						fillColor: '#4a5771',
						lineWidth: 2
					}
				}
			}
			chartConfig();
			$('#d_chart_box').highcharts(chartsData);

		function chartStart() {

			var chartStateLayer = {
				STATE : seriesSTATE,
				_setClose : false,
				init : function(state){
					var me = this,
					cookieId,
					now = new Date(),
					_isOpen1 = WEBSVC.Cookie.get('d_chart_L'),
					_isOpen2 = WEBSVC.Cookie.get('d_chart_L2');
					me.$items = $('#d_chart_L').add($('#d_chart_L2'));
					me.$items.each(function(){
						var item = $(this);
						item.find('.d_close').click(function(){
							cookieId = $(this).parents('.rank_layer').attr('id');
							var expiresDay = new Date();
							expiresDay.setMinutes(59);
							expiresDay.setSeconds(59);
							WEBSVC.Cookie.set(cookieId, now.getHours(), {expires : expiresDay});
							item.hide();
						})
					});
					if (me.STATE.length == 0) {
						return;
					}else if (me.STATE.length > 5 && _isOpen1 != now.getHours() && _isOpen2 != now.getHours()) {
						me.$items.show();
					}else if (me.STATE == "경합 중" && _isOpen1 != now.getHours()) {
						if (_isOpen1 != now.getHours()) {
							me.$items.eq(0).show();
						};
					}else if (me.STATE == "차트 올킬" && _isOpen2 != now.getHours()) {
						if (_isOpen2 != now.getHours()) {
							me.$items.eq(1).show();
						};
					};
				},
				hide : function() {
					$('#d_chart_L').hide();
					$('#d_chart_L2').hide();
				}
			};
			chartStateLayer.init();

			(function(){
				function pushRankArray(series){
					var rankState = {
						upRankArr : [],
						vIndexArr : [3,4,5],
						nowRankArr : []
					}
					var rankval = [];
					var prevRankval = [];
					var arrRank = {x : 0, y : [], _y : []}, _tmpPoint,
						_series = JSON.parse(JSON.stringify(series));

					function rankChange() {
						for (var i = 0,len = _series.length; i < len; i++){
							var t =0, tmpval, prevTmpval;
							_tmpPoint = _series[i].data;
							_tmpPoint.reverse();
							tmpval = (typeof _tmpPoint[0] != 'number') ? _tmpPoint[0].y : _tmpPoint[0];
							prevTmpval = (typeof _tmpPoint[1] != 'number') ? _tmpPoint[1].y : _tmpPoint[1];
							while(tmpval == 0){
								t++;
								tmpval = (typeof _tmpPoint[t] != 'number') ? _tmpPoint[t].y : _tmpPoint[t];
							}
							if(i>2){
								rankState.upRankArr.push(i);
							}
							rankval.push(tmpval);
							prevRankval.push(prevTmpval);
						}
					}
					function rankingChk() {
						var rankingClone = [], ranking_end = [],rankIdx,rank,rankOver,j=0;
						for(var i=0,len = _series.length; i<len; i++){
							rankingClone[i] = rankval[i];
						};
						while(rankingClone.length > 0) {
							var overlapIdx = [],rankOverlap = [],rankOverlapSlice = [];
							if (rankingClone.length == 1) {
								rank = rankingClone[0];
							}else {
								rank = Math.max.apply(null,rankingClone);
							};
							$(rankval).each(function(index) {
								if (this == rank) {
									rankIdx = index;
									overlapIdx.push(index);
									rankOverlap.push(prevRankval[rankIdx]);
									rankOverlapSlice.push(prevRankval[rankIdx]);
								};
							});
							if (rankOverlap.length > 1) {
								while(rankOverlapSlice.length > 0) {
									if (rankOverlapSlice.length == 1) {
										rankOver = rankOverlapSlice[0];
									}else {
										rankOver = Math.min.apply(null,rankOverlapSlice);
									};

									rankIdx = overlapIdx[$.inArray(rankOver, rankOverlap)];
									ranking_end[rankIdx] = (j+1);
									j++;
									rankOverlapSlice = $.grep(rankOverlapSlice, function(a) {
										return a > rankOver;
									});
								};
							}else {
								ranking_end[rankIdx] = (j+1);
								j++;
							};
							rankingClone = $.grep(rankingClone, function(a) {
								return a < rank;
							});
						};
						for(var i=0,len = _series.length; i<len; i++){
							if(ranking_end[i] > 3){
								rankState.nowRankArr.push(i);
							}
						}
						seriesRankingState = ranking_end;
					}
					rankChange();
					rankingChk();

					return rankState;
				}

				var realTimeChart = $('#d_chart_box'),
					charts = realTimeChart.highcharts(),
					charts2,
					chartIdx = 0,
					chartsData2,
					chartTimer = null,
					moreAreaBox = $('div.real_graph div.graph_bar');

				function createRankArray(series){
					var arrRankPosition = {x : 0, y : [], _y : []}, _tmpPoint, _series = series;

					for(var i=0; i<_series.length; i++){
						_tmpPoint = _series[i].graphPath;
						arrRankPosition._y.push(parseInt((_tmpPoint[5]+"").split('.')[0]));
						if(typeof _tmpPoint[0] =="string"){ _tmpPoint.reverse() };
						arrRankPosition.y.push(parseInt((_tmpPoint[0]+"").split('.')[0]));
					}
					arrRankPosition.x = parseInt((_tmpPoint[1]+"").split('.')[0]);

					return arrRankPosition;
				}
				var _rankState = pushRankArray(fiveSeries);
				function chartRankInit(sTarget){
					$(sTarget +' .d_icon_rank').remove();

					var _x = 0;
					var jSeries = realTimeChart.highcharts().series;

					if(sTarget == "#d_chart_box2"){
						jSeries = charts2.series;
						_x = -40;
					}
					var gradePos = createRankArray(jSeries);

					for(var i=0, len = jSeries.length; i<len; i++){

						if(i<3){
							if(sTarget == "#d_chart_box2"){
								if(seriesRankingState[i] < 4){
									$('#series'+fiveSeries[$.inArray(seriesRankingState[i], seriesRankingState)].name).addClass('forecast'+(i+1)).find('.d_rank_tmp').removeClass().addClass('rank_0'+seriesRankingState[i]).text(seriesRankingState[i]);//140527_순위처리
								}
								$('<a href="#" class="d_icon_rank d_rank'+(i+1)+' forecast'+seriesRankingState[i]+'">'+seriesRankingState[i]+'위 예측"</a>').appendTo(sTarget).css({
									position : 'absolute',
									left : gradePos.x + 16 + _x,
									top : gradePos.y[i] - 3,
									zIndex : 0
								});
							}else{
								$('<a href="#" class="d_icon_rank d_rank'+(i+1)+'">'+(i+1)+'위"</a>').appendTo(sTarget).css({
									position : 'absolute',
									left : gradePos.x + 16 + _x,
									top : gradePos.y[i] + 1,
									zIndex : 0
								});
							}
						} else {

							if(seriesRankingState[i] < 4){
								$('#series'+fiveSeries[$.inArray(seriesRankingState[i], seriesRankingState)].name).addClass('forecast'+(seriesRankingState[i]+3)).find('.d_rank_tmp').removeClass().addClass('rank_0'+seriesRankingState[i]).text(seriesRankingState[i]);//140515_순위처리
							}
							$('<a href="#" class="d_icon_rank d_new'+seriesRankingState[i]+'">'+seriesRankingState[i]+'위 예측</a>').appendTo(sTarget).css({
								position : 'absolute',
								left : gradePos.x + 16 + _x,
								top : gradePos.y[i] - 9,
								zIndex : 0
							})
							if((_rankState.nowRankArr[(i-3)]+1) == 1){
								$(sTarget).find('.d_icon_rank.d_new1').addClass('mhover');
							}
						}
					}
					var activeFn = function(e){
						e.preventDefault();
						var idx = $(this).index();
						chartExp.change(idx-1);
						chartExp.prevIdx = idx-1;
					}
'''
												


source = open('melon.html', 'rt', encoding='utf8').read()





# 1) rank
rank_pattern = re.compile(r'rank ">(\d{1,})</span>')
rank_content = re.findall(rank_pattern, source)
# print(rank_content)

# 2) title
title_pattern = re.compile(r';" title="(.*?)\s재생">')
title_content = re.findall(title_pattern, source)
# print(title_content)

# 3) artist
artist_pattern = re.compile(r'checkEllipsis.*?goArtistDetail.*?- 페이지 이동" >(.*?)</a>', re.DOTALL)
artist_content = re.findall(artist_pattern, source)
# print(artist_content)                                     # 왜 findall로 해서 두번 나오는 것을 또 걸러줬는지 의문
                                                            # 더 의문은 아래서는 또 search로 했다는것.. ;; ???
# 4) album                                                  # 스트링으로 뽑으려고 search로 바꿈 ㅡ_ㅡ;;
album_pattern = re.compile(r'ellipsis rank03".*?- 페이지 이동">(.*?)</a>', re.DOTALL)
album_content = re.findall(album_pattern, source)
# print(album_content)

# 이유는 모르겠지만 코드 상에서 찾을 수 없음.
# # 5) like
# like_pattern = re.compile(r'총건수</span>\n(.*?|,?)</span>', re.DOTALL)
# result5 = re.findall(like_pattern, source)
# print(result5)



# <tr> finditer로 match객체 찾기
tr_pattern = re.compile(r'<(tr class="lst50".*?)</tr>', re.DOTALL)
tr_iter = re.finditer(tr_pattern, source)

# 출력으로 tr코드 확인
# num = 1
# for i in tr_iter:
#     print(i.group())
#     print(f'{num}순위 tr 코드 가져오기')
#     num += 1



# 1) 수업시간에 못해본 1줄 리스트 출력해보기 by re.findall
# for i in tr_iter:
#     print( re.findall(rank_pattern, i.group()), end = '')
#     print( re.findall(title_pattern, i.group()), end = '' )
#     print( re.findall(artist_pattern, i.group()), end = '' )
#     print( re.findall(album_pattern, i.group()), end = '\n' )


# 2) 수업시간에 못해본 1줄 리스트 출력해보기 by re.search
# for i in tr_iter:
#     print( re.search(rank_pattern, i.group()).group(1), end = ' ')
#     print( re.search(title_pattern, i.group()).group(1), end = ' ' )
#     print( re.search(artist_pattern, i.group()).group(1), end = ' ' )
#     print( re.search(album_pattern, i.group()).group(1), end = '\n' )


# 3) 딕셔너리에 넣기

# melon_chart = list()
# melon_dict = dict()
#
#
# for i in tr_iter:
#     melon_dict['rank'] = re.search(rank_pattern, i.group()).group(1)
#     melon_dict['title'] = re.search(title_pattern, i.group()).group(1)
#     melon_dict['artist'] = re.search(artist_pattern, i.group()).group(1)
#     melon_dict['album'] = re.search(album_pattern, i.group()).group(1)
#     melon_chart.append(melon_dict)
#     # print(melon_chart)
#
# # print(melon_dict2) # 마지막 melon_dict 확인


# 4) 문제 굉장히 지저분하게 해결.
#
# melon_chart = list()
# melon_dict = dict()
# melon_dict2 = dict()
#
#
# for i in tr_iter:
#     melon_dict['rank'] = re.search(rank_pattern, i.group()).group(1)
#     melon_dict['title'] = re.search(title_pattern, i.group()).group(1)
#     melon_dict['artist'] = re.search(artist_pattern, i.group()).group(1)
#     melon_dict['album'] = re.search(album_pattern, i.group()).group(1)
#     # 딕셔너리에 잘 들어갔는지 확인
#     melon_dict2 = melon_dict.copy()
#     melon_chart.append(melon_dict2)
#     melon_dict.clear()                     # 1) 딕셔너리에 같은게 계속 들어가서 덮어씌워지고 있었음?
#     # 리스트에 딕셔너리가 잘 들어갔는지 확인         # 2) 그런데 .clear() 함수를 쓰면 리스트에 들어간 놈들까지 다 없어짐 ;;;
#     # print(melon_chart)                   # 3) 아마 리스트안의 것들의 참조값이 같았던 모양..
#                                            # 4) deep copy를 하는 .copy() 함수로 겨우 해결.
#
# # print(melon_dict2) # 마지막 melon_dict 확인



## 딕셔너리 50개의 객체가 아니라 들어갈때 같은 딕셔너리에 내용이 덮어서 들어갈때 그렇게 된것.












# 1) rank
rank_pattern = re.compile(r'rank ">(\d{1,})</span>')
rank_content = re.findall(rank_pattern, source)
# print(rank_content)

# 2) title
title_pattern = re.compile(r';" title="(.*?)\s재생">')
title_content = re.findall(title_pattern, source)
# print(title_content)

# 3) artist
artist_pattern = re.compile(r'checkEllipsis.*?goArtistDetail.*?- 페이지 이동" >(.*?)</a>', re.DOTALL)
artist_content = re.findall(artist_pattern, source)
# print(artist_content)                                     # 왜 findall로 해서 두번 나오는 것을 또 걸러줬는지 의문
                                                            # 더 의문은 아래서는 또 search로 했다는것.. ;; ???
# 4) album                                                  # 스트링으로 뽑으려고 search로 바꿈 ㅡ_ㅡ;;
album_pattern = re.compile(r'ellipsis rank03".*?- 페이지 이동">(.*?)</a>', re.DOTALL)
album_content = re.findall(album_pattern, source)
# print(album_content)




# 5) 딕셔너리 생성하는 위치 바꾸기 - 위치 하나로 위의 모든 불필요한 과정 생략.


melon_chart = list()


for i in tr_iter:
    melon_dict = dict()

    melon_dict['rank'] = re.search(rank_pattern, i.group()).group(1)
    melon_dict['title'] = re.search(title_pattern, i.group()).group(1)
    melon_dict['artist'] = re.search(artist_pattern, i.group()).group(1)
    melon_dict['album'] = re.search(album_pattern, i.group()).group(1)
    # 딕셔너리에 잘 들어갔는지 확인
    melon_chart.append(melon_dict)
    # 리스트에 딕셔너리가 잘 들어갔는지 확인
    print(melon_chart)

# print(melon_dict) # 마지막 melon_dict 확인




# 최종결과 확인
# 1줄씩 출력
for i in range(0, len(melon_chart)):
    print( melon_chart[i] )

# 리스트 통째로 출력
# print(melon_chart)






# example1 = '<a href="https://google.co.kr">Google</a>'
# source = '''
# <div class="first-div">
#     <div class="second-div">
#         <span class="span-content">ABCD</span>
#     </div>
# </div>
# '''
#
#
# def get_tag_attribute(attribute_name, tag_string):
#
#
#     p_first_tag = re.compile(r'^.*?<.*?>', re.DOTALL)
#     first_tag = p_first_tag.search(tag_string).group()
#
#     # p = re.compile(r'{attribute_name}="(.*?)"')   # 하다 박살.
#     p = re.compile(r'^.*?<.*?{attribute_name}="(?P<value>.*?)".*?>'.format(
#         attribute_name=attribute_name
#     ), re.DOTALL)
#     m = p.search(first_tag)
#     if m:
#         # print(m.group())
#         return m.group('value')
#     return '없다'
#
#
# result = get_tag_attribute('class', source)
# print(result)
#
#
#
# def get_tag_content(tag_string):
#     p = re.compile(r'.*?<.*?">(?P<value>.*?)</.*?>')
#     m = p.search(tag_string)
#     if m:
#         return m.group('value')
#     return ''
#
# result2 = get_tag_content(source)
# print(result2)