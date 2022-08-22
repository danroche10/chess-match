from chess.helpers import Helpers

def test_get_updated_valid_moves():
  moves = {}
  updated_moves = Helpers.get_updated_valid_moves(moves, 4, 3)
  assert updated_moves == {(4,3) : []}
