from PIL import Image
import numpy as np
import os

def create_slider_animation(old_logo_path, new_logo_path, output_path, duration=8000, fps=30, size=(1200, 1200), max_frames=250):
    # Load images
    old_logo = Image.open(old_logo_path).convert('RGBA')
    new_logo = Image.open(new_logo_path).convert('RGBA')
    
    width, height = size
    old_logo = old_logo.resize((width, height), Image.Resampling.LANCZOS)
    new_logo = new_logo.resize((width, height), Image.Resampling.LANCZOS)
    
    # Calculate total frames (capped at max_frames)
    total_frames = min(int(duration / 1000 * fps), max_frames)
    
    # Create frames
    frames = []
    for i in range(total_frames):
        # Calculate progress (0 to 1 and back)
        progress = abs((i / (total_frames - 1)) * 2 - 1)
        
        # Create new frame
        frame = Image.new('RGBA', (width, height), (255, 255, 255, 0))
        
        # Calculate split position
        split_pos = int(width * progress)
        
        # Paste old logo
        frame.paste(old_logo, (0, 0))
        
        # Paste new logo with mask
        mask = Image.new('L', (width, height), 0)
        mask_draw = Image.new('L', (width, height), 255)
        mask.paste(mask_draw, (split_pos, 0))
        frame.paste(new_logo, (0, 0), mask)
        
        frames.append(frame.convert('P', palette=Image.ADAPTIVE))
    
    # Save as GIF
    frames[0].save(
        output_path,
        save_all=True,
        append_images=frames[1:],
        duration=int(1000/(total_frames/duration*1000)),
        loop=0,
        optimize=True
    )

# To Create the animation
# Add your file names in place of A.png and B.png. Make sure they are in the same folder as this script.
# Add your output file name in place of logo_comparison_AB.gif


create_slider_animation(
    'A.png',
    'B.png',
    'logo_comparison_AB.gif',
    duration=8000, # 8 seconds for a full cycle (quarter speed)
    fps=30,        # 30 frames per second
    size=(1200, 1200),
    max_frames=250
) 