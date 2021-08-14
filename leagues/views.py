from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
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
		"jugador_alexander_o_wyatt": Player.objects.filter(first_name__contains = ["Alexander", "wyatt"]),



	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")