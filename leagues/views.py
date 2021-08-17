from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Q
from django.db.models import Count

from . import team_maker

def index(request):
	context = {
		#Consultas ejercicio 1
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
		"liga_mujeres": League.objects.filter(name__contains = "womens"),
		"liga_hockey": League.objects.filter(sport__contains = "hockey"),
		"liga_no_football": League.objects.exclude(sport__contains = "football"),
		"liga_conferencia": League.objects.filter(name__contains = "conference"),
		"liga_atlantica": League.objects.filter(name__contains = "Atlantic"),
		"equipo_dallas": Team.objects.filter(location__contains = "Dallas"),
		"equipo_raptors": Team.objects.filter(team_name__contains = "Raptors"),
		"equipo_city": Team.objects.filter(location__contains = "City"),
		"equipo_t": Team.objects.filter(team_name__startswith = "t"),
		"equipo_orden_ubicacion": Team.objects.all().order_by('location'),
		"equipo_orden_nombre": Team.objects.all().order_by('-team_name'),
		"jugador_cooper": Player.objects.filter(last_name__contains = "cooper"),
		"jugador_joshua": Player.objects.filter(first_name__contains = "joshua"),
		"jugador_cooper_no_joshua": Player.objects.filter(last_name__contains = "cooper").exclude(first_name__contains = "joshua"),
		"jugador_alexander_o_wyatt": Player.objects.filter(first_name__contains = "Alexander") | Player.objects.filter(first_name__contains = "wyatt"),
		"jugador_alexander_o_wyatt2": Player.objects.filter(Q(first_name = "Alexander") | Q(first_name = "Wyatt")),

		#Consultas ejercicio 2
		"equipo_atlantic": Team.objects.filter(league__name__contains = "Atlantic")& Team.objects.filter(league__name__contains = "Soccer")&Team.objects.filter(league__name__contains = "Conference"),
		"jugador_boston_penguins": Player.objects.filter(curr_team__location__contains = "Boston") | Player.objects.filter(curr_team__location__contains = "Penguins"),
		"jugador_international": Player.objects.filter(curr_team__league__name="International Collegiate Baseball Conference"),
		"jugador_conferencia": Player.objects.filter(Q(curr_team__league__name="American Conference of Amateur Football") & Q(last_name = "Lopez")),
		"jugador_soccer": Player.objects.filter(Q(curr_team__league__name__contains="Soccer")),
		"equipo_sophia": Team.objects.filter(curr_players__first_name = "Sophia"),
		"liga_sophia": League.objects.filter(teams__curr_players__first_name = "Sophia"),
		"jugador_flores": Player.objects.filter(last_name__contains="flores").exclude(curr_team__location__contains="Washington").exclude(curr_team__location__contains="Roughriders"),
		"equipo_samuel": Team.objects.filter(all_players__first_name = "Samuel"),
		"jugador_manitoba": Player.objects.filter(Q(all_teams__location__contains="Manitoba")|Q(all_teams__location__contains="Tiger-Cats")),
		"jugador_wichita": Player.objects.filter(all_teams__location__contains="Wichita").exclude(curr_team__location__contains="Wichita"),
		"equipo_jacob": Team.objects.filter(all_players__first_name = "Jacob").filter(all_players__last_name = "Gray").exclude(team_name__contains = "Colts"),
		"jugador_joshua": Player.objects.filter(first_name__contains="Joshua").filter(all_teams__league__name="Atlantic Amateur Field Hockey League"),
		"q": Team.objects.annotate(Count('all_players__id')),
		#"equipo_doce": Team.objects.filter(team12__gte=12),
	
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")