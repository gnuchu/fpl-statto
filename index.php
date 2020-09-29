<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Document</title>
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
<link rel="stylesheet" href="https://cdn.datatables.net/1.10.22/css/jquery.dataTables.min.css">
<link rel="stylesheet" href="assets/css/custom.css">

<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha256-4+XzXVhsDmqanXGHaHvgh1gMQKX40OUvDEBTu8JcmNs=" crossorigin="anonymous"></script>
<script src="https://cdn.datatables.net/1.10.22/js/jquery.dataTables.min.js"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.bundle.min.js" integrity="sha384-LtrjvnR4Twt/qOuYxE721u19sVFLVSA4hf/rRt6PrZTmiPltdZcI7q7PXQBYTKyf" crossorigin="anonymous"></script>
</head>
<body>

<script>
  $(document).ready( function () {
    $('.player_info').DataTable({
      paging: false,
      searching: false,
      bInfo: false
    });
  });
</script>

<div class='container'><h2>Goalkeepers</h2><br/><table class='table table-striped table-hover table-sm player_info'>
  <thead class='thead-dark'>
  <th>Player</th>
  <th>Team</th>
  <th>Postion</th>
  <th>Current Cost</th>
  <th>Value</th>
  <th>Total Points</th>
  </thead>
  <tbody><tr><td>Martínez</td><td>Aston Villa</td><td>GKP</td><td>45</td><td>4.2</td><td>19</td></tr><tr><td>Darlow</td><td>Newcastle</td><td>GKP</td><td>50</td><td>3.4</td><td>17</td></tr><tr><td>Guaita</td><td>Crystal Palace</td><td>GKP</td><td>50</td><td>3.0</td><td>15</td></tr><tr><td>Meslier</td><td>Leeds</td><td>GKP</td><td>45</td><td>2.9</td><td>13</td></tr><tr><td>Ramses Becker</td><td>Liverpool</td><td>GKP</td><td>60</td><td>2.8</td><td>17</td></tr><tr><td>Leno</td><td>Arsenal</td><td>GKP</td><td>50</td><td>2.4</td><td>12</td></tr><tr><td>Pickford</td><td>Everton</td><td>GKP</td><td>50</td><td>2.2</td><td>11</td></tr><tr><td>Ryan</td><td>Brighton</td><td>GKP</td><td>45</td><td>1.8</td><td>8</td></tr><tr><td>Fabianski</td><td>West Ham</td><td>GKP</td><td>50</td><td>1.8</td><td>9</td></tr><tr><td>dos Santos Patrício</td><td>Wolves</td><td>GKP</td><td>55</td><td>1.8</td><td>10</td></tr></div></tbody></table><h2>Defenders</h2><br/><table class='table table-striped table-hover table-sm player_info'>
  <thead class='thead-dark'>
  <th>Player</th>
  <th>Team</th>
  <th>Postion</th>
  <th>Current Cost</th>
  <th>Value</th>
  <th>Total Points</th>
  </thead>
  <tbody><tr><td>Castagne</td><td>Leicester</td><td>DEF</td><td>57</td><td>4.7</td><td>27</td></tr><tr><td>Konsa Ngoyo</td><td>Aston Villa</td><td>DEF</td><td>45</td><td>4.7</td><td>21</td></tr><tr><td>Mings</td><td>Aston Villa</td><td>DEF</td><td>50</td><td>4.4</td><td>22</td></tr><tr><td>Justin</td><td>Leicester</td><td>DEF</td><td>47</td><td>3.6</td><td>17</td></tr><tr><td>Magalhães</td><td>Arsenal</td><td>DEF</td><td>51</td><td>3.3</td><td>17</td></tr><tr><td>Saïss</td><td>Wolves</td><td>DEF</td><td>51</td><td>3.1</td><td>16</td></tr><tr><td>Digne</td><td>Everton</td><td>DEF</td><td>61</td><td>3.1</td><td>19</td></tr><tr><td>James</td><td>Chelsea</td><td>DEF</td><td>51</td><td>3.1</td><td>16</td></tr><tr><td>Keane</td><td>Everton</td><td>DEF</td><td>50</td><td>3.0</td><td>15</td></tr><tr><td>Masuaku</td><td>West Ham</td><td>DEF</td><td>45</td><td>2.9</td><td>13</td></tr></div></tbody></table><h2>Midfielders</h2><br/><table class='table table-striped table-hover table-sm player_info'>
  <thead class='thead-dark'>
  <th>Player</th>
  <th>Team</th>
  <th>Postion</th>
  <th>Current Cost</th>
  <th>Value</th>
  <th>Total Points</th>
  </thead>
  <tbody><tr><td>Sousa de Azevedo e Costa</td><td>Leeds</td><td>MID</td><td>56</td><td>3.9</td><td>22</td></tr><tr><td>Klich</td><td>Leeds</td><td>MID</td><td>56</td><td>3.8</td><td>21</td></tr><tr><td>Townsend</td><td>Crystal Palace</td><td>MID</td><td>60</td><td>3.7</td><td>22</td></tr><tr><td>Hendrick</td><td>Newcastle</td><td>MID</td><td>50</td><td>3.6</td><td>18</td></tr><tr><td>Zaha</td><td>Crystal Palace</td><td>MID</td><td>72</td><td>3.3</td><td>24</td></tr><tr><td>Son</td><td>Spurs</td><td>MID</td><td>90</td><td>3.0</td><td>27</td></tr><tr><td>Bowen</td><td>West Ham</td><td>MID</td><td>63</td><td>3.0</td><td>19</td></tr><tr><td>Harrison</td><td>Leeds</td><td>MID</td><td>55</td><td>2.9</td><td>16</td></tr><tr><td>Praet</td><td>Leicester</td><td>MID</td><td>55</td><td>2.9</td><td>16</td></tr><tr><td>Hourihane</td><td>Aston Villa</td><td>MID</td><td>60</td><td>2.8</td><td>17</td></tr></div></tbody></table><h2>Forwards</h2><br/><table class='table table-striped table-hover table-sm player_info'>
  <thead class='thead-dark'>
  <th>Player</th>
  <th>Team</th>
  <th>Postion</th>
  <th>Current Cost</th>
  <th>Value</th>
  <th>Total Points</th>
  </thead>
  <tbody><tr><td>Bamford</td><td>Leeds</td><td>FWD</td><td>58</td><td>5.0</td><td>29</td></tr><tr><td>Calvert-Lewin</td><td>Everton</td><td>FWD</td><td>74</td><td>4.2</td><td>31</td></tr><tr><td>Maupay</td><td>Brighton</td><td>FWD</td><td>65</td><td>4.0</td><td>26</td></tr><tr><td>Vardy</td><td>Leicester</td><td>FWD</td><td>100</td><td>3.2</td><td>32</td></tr><tr><td>Robinson</td><td>West Brom</td><td>FWD</td><td>55</td><td>2.9</td><td>16</td></tr><tr><td>Wilson</td><td>Newcastle</td><td>FWD</td><td>64</td><td>2.8</td><td>18</td></tr><tr><td>de Andrade</td><td>Everton</td><td>FWD</td><td>80</td><td>2.8</td><td>22</td></tr><tr><td>Kane</td><td>Spurs</td><td>FWD</td><td>105</td><td>2.7</td><td>28</td></tr><tr><td>Ings</td><td>Southampton</td><td>FWD</td><td>84</td><td>2.6</td><td>22</td></tr><tr><td>Mitrović</td><td>Fulham</td><td>FWD</td><td>60</td><td>2.5</td><td>15</td></tr></div></tbody></table></div></body></html>