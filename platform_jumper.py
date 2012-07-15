# Sample Python/Pygame Programs
# Simpson College Computer Science
# http://cs.simpson.edu
import os
import pygame
import random
from imcombine import imcombine
from play import StaticAniSprite
# Define some colors
black = ( 0, 0, 0)
white = ( 255, 255, 255)
red = ( 255, 0, 0)
# This class represents the platform we jump on
class Platform (pygame.sprite.Sprite):
	def __init__(self, color, width, height):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([width, height])
		self.image.fill(color)
		self.rect = self.image.get_rect()
# This class represents the bar at the bottom that the player controls
class Player(pygame.sprite.Sprite):
	# -- Attributes
	# Set speed vector of player
	change_x=0
	change_y=0
	# Triggered if the player wants to jump.
	jump_ready = False
	# Count of frames since the player hit 'jump' and we
	# collided against something. Used to prevent jumping
	# when we haven't hit anything.
	frame_since_collision = 0
	frame_since_jump = 0
	# -- Methods
	# Constructor function
	def __init__(self,x,y,isize,path,fname,screen):
		#screen size
		self.screen=screen
		#image size
		self.isize=isize
		# Call the parent's constructor
		pygame.sprite.Sprite.__init__(self)
		# Set height, width
		self.image = pygame.Surface([self.isize,self.isize])
		#self.image.fill((red))
		self.fname=fname
		self.path=path
		bgcb=imcombine(self.fname,self.path)
		self.bgim=StaticAniSprite(bgcb,15)
		self.bgim.render(self.image)
		# Make our top-left corner the passed-in location.
		self.rect = self.image.get_rect()
		self.rect.topleft = [x,y]
		# Change the speed of the player
	def changespeed_x(self,x):
		self.change_x = x
	def changespeed_y(self,y):
		self.change_y = y
	# Find a new position for the player
	def update(self,blocks):
		# Save the old x position, update, and see if we collided.
		old_x = self.rect.left
		print 'old_x:',old_x
		new_x = old_x + self.change_x
		print 'new_x',new_x
		if old_x!=new_x:
			self.bgim.render(self.image)
		self.rect.left = new_x
		collide = pygame.sprite.spritecollide (self, blocks, False)
		if collide:
		# We collided, go back to the old pre-collision location
			self.rect.left = old_x
		# Save the old y position, update, and see if we collided.
		old_y = self.rect.top
		new_y = old_y + self.change_y
		self.rect.top = new_y
		block_hit_list = pygame.sprite.spritecollide(self, blocks, False)
		for block in block_hit_list:
			# We collided. Set the old pre-collision location.
			self.rect.top = old_y
			self.rect.x = old_x
			# Stop our vertical movement
			self.change_y = 0
			# Start counting frames since we hit something
			self.frame_since_collision = 0
			# If the player recently asked to jump, and we have recently
			# had ground under our feet, go ahead and change the velocity
			# to send us upwards
		if self.frame_since_collision < 6 and self.frame_since_jump < 6:
			self.frame_since_jump = 100
			self.change_y -= 8
		# Increment frame counters
		self.frame_since_collision+=1
		self.frame_since_jump+=1
	# Calculate effect of gravity.
	def calc_grav(self):
		self.change_y += .35
		# See if we are on the ground.
		if self.rect.top >= self.screen[1]-self.isize and self.change_y >= 0:
			self.change_y = 0
			self.rect.top = self.screen[1]-self.isize
			self.frame_since_collision = 0
	# Called when user hits 'jump' button
	def jump(self,blocks):
		self.jump_ready = True
		self.frame_since_jump = 0
		self.bgim.render(self.image)
pygame.init()
# Set the height and width of the screen
size=[700,500]
screen=pygame.display.set_mode(size)
pygame.display.set_caption("JUMP!")
# Create platforms
def create_level1(block_list,all_sprites_list):
	# 7 blocks
	for i in range(7):
		block = Platform(white, 80, 20)
		# Set x and y based on block number
		if i != 0:
			block.rect.x = 75 * i
			block.rect.y = 75 * i
			block_list.add(block)
			all_sprites_list.add(block)
# Main program, create the blocks
block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
create_level1(block_list,all_sprites_list)
player = Player(0,0,150,os.getcwd()+'/data','halo',size)
#340,485
player.rect.x = 0
player.rect.y = 350
all_sprites_list.add(player)
#Loop until the user clicks the close button.
done=False
# Used to manage how fast the screen updates
clock=pygame.time.Clock()
ti=40
# -------- Main Program Loop -----------
while done==False:
	for event in pygame.event.get(): # User did something
		if event.type == pygame.QUIT: # If user clicked close
			done=True # Flag that we are done so we exit this loop
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				print 'k_left'
				player.changespeed_x(-2)
			if event.key == pygame.K_RIGHT:
				print 'k_right'
				player.changespeed_x(2)
			if event.key == pygame.K_UP:
				print 'k_up'
				player.jump(block_list)
			if event.key == pygame.K_DOWN:
				print 'k_down'
				player.changespeed_y(10)
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				player.changespeed_x(-0)
			if event.key == pygame.K_RIGHT:
				player.changespeed_x(0)
	# Wrap player around the screen if they go too far left/right
	if player.rect.x >= size[0]-player.isize:
		player.rect.x = size[0]-player.isize
	if player.rect.x <= 0:
		player.rect.x = 0
	player.calc_grav()
	player.update(block_list)
	block_list.update()
	# Set the screen background
	screen.fill(black)
	# ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
	all_sprites_list.draw(screen)
	# ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
	# Limit to 20 frames per second
	clock.tick(ti)
	# Go ahead and update the screen with what we've drawn.
	pygame.display.flip()
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit ()
