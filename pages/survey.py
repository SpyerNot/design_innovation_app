import streamlit as st
import random as rd
exercise_obese_teens = ['Goal: Improve cardiovascular health and flexibility.Duration: 30 minutes/day, 5 days/week.Week Layout: Day 1-5:Warm-up: 5 minutes of brisk walking.Main Exercise: 20 minutes of moderate walking.Cool-down: 5 minutes of full-body stretching.Day 6-7: Rest or light stretching.','Goal: Increase heart rate without putting too much strain on joints.Duration: 30-40 minutes/day, 4 days/week.Week Layout: Day 1 & 3: Warm-up: 5 minutes of marching in place.Main Exercise: 20 minutes of low-impact aerobics (step-touch, side-steps, light dance moves).Cool-down: 5 minutes of stretching.Day 2 & 4:20 minutes of gentle swimming or water walking (if available).Day 5-7: Rest or light stretching.','Goal: Build strength using bodyweight exercises.Duration: 20-30 minutes/day, 3 days/weekWeek Layout: Day 1, 3, 5: Warm-up: 5 minutes of walking. Circuit (3 rounds with 1-minute rest between rounds):10 squats,10 wall push-ups,10-second plank,10 glute bridges.Cool-down: 5 minutes of stretching. Day 2, 4, 6-7: Rest or light walking.','Goal: Make exercise fun with dance routines. Duration: 20-30 minutes/day, 5 days/week. Week Layout: Day 1-5: Warm-up: 5 minutes of light dancing. Main Exercise: 20 minutes of following a simple dance workout (YouTube, or a dance-based app). Cool-down: 5 minutes of stretching. Day 6-7: Rest or casual dance for fun.']
exercise_overweight_teens = ['Exercise Plan: Day 1: 30-minute brisk walk + 15-minute bodyweight exercises (squats, lunges, push-ups). Day 2: 20-minute light jogging + 10-minute stretching (hamstrings, quads, calves). Day 3: Rest day or gentle yoga (20 minutes). Day 4: 30-minute cycling or swimming + 10-minute core workout (plank, crunches). Day 5: 20-minute interval running (30 sec sprint/1 min walk) + 15-minute strength workout (planks, burpees). Day 6: Fun outdoor activity (soccer, basketball, or dance) for 45 minutes.Day 7: Rest or 15-minute yoga/stretching. Eating Plan: Breakfast: Greek yogurt with mixed berries and a handful of oats. Lunch: Grilled chicken wrap with whole grain tortillas, veggies, and a light dressing. Snack: Apple slices with almond butter. Dinner: Baked salmon with quinoa and steamed vegetables. Hydration: Drink 6-8 cups of water a day. Limit: Sugary drinks and processed snacks','Exercise Plan: Day 1: 25-minute run + 15-minute bodyweight circuit (push-ups, squats, plank). Day 2: Rest or 30 minutes of stretching/yoga. Day 3: 30-minute strength workout (using light weights or resistance bands). Day 4: 40-minute brisk walk or moderate cycling. Day 5: High-intensity interval training (HIIT): 20 seconds work, 40 seconds rest, for 25 minutes (jumping jacks, squats, mountain climbers). Day 6: 45-minute swimming or dancing. Day 7: Active recovery day (light walk or stretching for 20 minutes). Eating Plan: Breakfast: Scrambled eggs with whole-grain toast and a side of fruit. Lunch: Turkey and avocado sandwich on whole wheat bread with side salad. Snack: A banana or handful of nuts. Dinner: Stir-fry tofu or chicken with brown rice and mixed veggies. Hydration: 6-8 cups of water daily. Limit: Fried and fast foods','Exercise Plan: Day 1: 40-minute light jog or power walk. Day 2: 25-minute stair climbing or hill sprints. Day 3: Rest or 20-minute yoga session. Day 4: 30-minute bike ride or rollerblading. Day 5: 45-minute dance workout (Zumba or any fun dance routines). Day 6: Play a sport of your choice (soccer, basketball, or tennis) for 60 minutes. Day 7: Rest or stretching (15 minutes).Eating Plan: Breakfast: Smoothie with spinach, banana, almond milk, and chia seeds. Lunch: Grilled chicken salad with mixed greens, avocado, and olive oil dressing. Snack: Mixed nuts or carrots with hummus. Dinner: Grilled lean beef or turkey burger (without bun) with a sweet potato and steamed vegetables. Hydration: 7-9 cups of water daily. Limit: Sugary treats and processed foods','Exercise Plan: Day 1: 20-minute jump rope session + 10 minutes of ab exercises (planks, crunches). Day 2: 30-minute bodyweight strength workout (lunges, squats, push-ups). Day 3: Rest or gentle stretching for 15 minutes. Day 4: 30-minute interval running (1 minute sprint, 2 minutes jog). Day 5: Strength training using light weights or resistance bands (20-25 minutes). Day 6: 45-minute brisk walk or swimming. Day 7: Fun outdoor activity (bike ride, hike, or sports) for 60 minutes. Eating Plan. Breakfast: Oatmeal with almond milk, nuts, and a drizzle of honey. Lunch: Whole grain pasta with grilled chicken, olive oil, and vegetables. Snack: Greek yogurt or fruit salad. Dinner: Baked chicken or turkey breast with roasted vegetables and brown rice. Hydration: 6-8 cups of water.Limit: Soda and sugary cereals','Exercise Plan: Day 1: 25-minute yoga/stretching session + 10 minutes of light bodyweight exercises. Day 2: 30-minute moderate-intensity cardio (jogging, biking). Day 3: Rest or stretching (15 minutes). Day 4: 40-minute swimming or brisk walk. Day 5: HIIT workout (jump squats, burpees, push-ups) for 20 minutes. Day 6: Fun sports activity (basketball, tennis, soccer) for 60 minutes.Day 7: Rest or stretching/yoga for 20 minutes.Eating Plan: Breakfast: Whole-grain cereal with almond milk and fresh fruit. Lunch: Tuna or chicken salad sandwich on whole-grain bread. Snack: A small handful of almonds or a piece of fruit. Dinner: Grilled fish with quinoa and sautéed vegetables. Hydration: 7-9 cups of water daily.Limit: Junk food and heavy sauces']
exercise_normal_teens = ['Exercise Plan: Day 1: 30-minute brisk walk or light jogging + 15 minutes of bodyweight exercises (push-ups, squats, lunges). Day 2: 20-minute moderate cycling + 10-minute stretching routine. Day 3: Rest day or 20 minutes of yoga. Day 4: 25-minute strength training (light weights or resistance bands) + 10 minutes of core exercises (planks, crunches). Day 5: 30-minute cardio (swimming, running, or dance workout). Day 6: Fun outdoor activity (soccer, basketball, or hiking) for 45-60 minutes. Day 7: Rest or 15 minutes of stretching. Eating Plan: Breakfast: Whole grain toast with scrambled eggs and avocado. Lunch: Grilled chicken or tofu salad with mixed greens, quinoa, and olive oil dressing. Snack: Sliced apple with peanut butter. Dinner: Baked salmon or chicken with brown rice and steamed vegetables. Hydration: 6-8 cups of water. Limit: Sugary snacks and drinks','Exercise Plan: Day 1: 25-minute moderate jogging + 10-minute bodyweight circuit (squats, lunges, planks). Day 2: 20-minute interval training (alternating between 1-minute sprint and 2-minute walking). Day 3: Rest day or 20-minute yoga/stretching. Day 4: 30-minute strength workout (focus on legs and core) using bodyweight or light weights. Day 5: 40-minute brisk walk or swimming. Day 6: Outdoor sports or activity (basketball, soccer, or cycling) for 45 minutes. Day 7: Rest day or light stretching (15-20 minutes). Eating Plan: Breakfast: Greek yogurt with mixed berries and oats. Lunch: Whole wheat pasta with grilled chicken and sautéed vegetables. Snack: A banana or handful of mixed nuts. Dinner: Grilled lean meat (chicken or turkey) with quinoa and steamed broccoli. Hydration: 6-8 cups of water.Limit: Processed foods and excessive fried snacks','Exercise Plan: Day 1: 30-minute light jog or power walk. Day 2: 20-minute stair climbing or hill sprints. Day 3: Rest or 15-minute yoga/stretching. Day 4: 25-minute cycling or rollerblading + 10-minute core workout. Day 5: 45-minute dance workout (Zumba or any fun dance routine). Day 6: Play a sport of choice (soccer, basketball, or tennis) for 60 minutes. Day 7: Rest or 15-minute flexibility/stretching exercises. Eating Plan. Breakfast: Smoothie with spinach, banana, almond milk, and chia seeds. Lunch: Turkey and cheese sandwich on whole-grain bread with a side salad. Snack: Veggies with hummus or a handful of nuts. Dinner: Baked fish or chicken with sweet potato and mixed steamed vegetables. Hydration: 6-8 cups of water. Limit: Sugary beverages and snacks','Exercise Plan: Day 1: 20-minute jump rope session + 15 minutes of core exercises (crunches, planks, leg raises). Day 2: 25-minute bodyweight strength training (lunges, squats, push-ups). Day 3: Rest day or 20-minute yoga/stretching. Day 4: 30-minute interval training (sprint 30 seconds, walk 1 minute). Day 5: 20-minute strength training (upper body focus) + 10-minute core workout. Day 6: 45-minute brisk walk or bike ride. Day 7: Active recovery (light stretching or yoga for 15-20 minutes). Eating Plan: Breakfast: Oatmeal with almond milk, walnuts, and honey. Lunch: Tuna or chicken salad wrap with whole grain tortillas and veggies. Snack: Greek yogurt or fruit smoothie. Dinner: Grilled turkey burger (without bun) with roasted vegetables and brown rice. Hydration: 6-8 cups of water. Limit: Sugary drinks and processed snacks','Exercise Plan: Day 1: 20-minute yoga or stretching session + 10 minutes of bodyweight exercises (lunges, squats, planks). Day 2: 30-minute light jogging or cycling. Day 3: Rest or 15 minutes of yoga/stretching. Day 4: 30-minute swimming or brisk walk + 10-minute core workout. Day 5: 20-minute HIIT (high-intensity interval training) + 10 minutes of stretching. Day 6: Fun sport (basketball, tennis, or hiking) for 45-60 minutes. Day 7: Rest or gentle stretching for 15-20 minutes. Eating Plan: Breakfast: Whole-grain cereal with almond milk and fresh fruit. Lunch: Grilled chicken wrap with lettuce, tomato, and light dressing. Snack: Carrot sticks with hummus or an apple. Dinner: Grilled lean meat (chicken or turkey) with brown rice and steamed veggies. Hydration: 7-9 cups of water daily. Limit: High-sugar and fried foods']
exercise_underweight_teens = ['Exercise Plan: Day 1: 30-minute brisk walk + 15-minute full-body bodyweight exercises (push-ups, squats, lunges). Day 2: 20-minute light jogging + 10-minute core workout (plank, crunches). Day 3: 25-minute strength training using light weights or resistance bands (focus on upper body). Day 4: Rest day or light stretching (15 minutes). Day 5: 30-minute moderate cardio (swimming, cycling, or brisk walking) + 10 minutes of ab exercises. Day 6: 40-minute outdoor sports (soccer, basketball, or hiking). Day 7: Rest day or yoga/stretching (15 minutes). Eating Plan: Breakfast: Scrambled eggs with whole grain toast, avocado, and a side of fruit. Lunch: Grilled chicken or tofu with quinoa and steamed vegetables. Snack: A banana with peanut butter. Dinner: Baked salmon or lean beef with brown rice and roasted vegetables. Hydration: 7-9 cups of water daily','Exercise Plan: Day 1: 30-minute cycling + 15-minute ab exercises (planks, leg raises, mountain climbers). Day 2: 25-minute interval running (1 minute sprint, 2 minutes walk). Day 3: Rest or gentle yoga/stretching (20 minutes). Day 4: 25-minute moderate jogging + 10-minute core workout. Day 5: 40-minute dance workout (Zumba or any fun cardio routine). Day 6: 30-minute swimming or power walking. Day 7: Rest or 20-minute light stretching. Eating Plan: Breakfast: Greek yogurt with mixed berries, honey, and a handful of granola. Lunch: Whole wheat pasta with grilled chicken and a light olive oil dressing. Snack: Trail mix with nuts and dried fruit. Dinner: Grilled chicken or fish with sweet potatoes and sautéed greens. Hydration: 6-8 cups of water daily','Exercise Plan: Day 1: 30-minute brisk walk + 15-minute stretching routine (hamstrings, quads, calves, back). Day 2: 20-minute moderate jog or cycling + 10 minutes of functional movements (jump squats, push-ups, lunges). Day 3: Rest or 15-minute yoga/stretching. Day 4: 30-minute HIIT workout (20 seconds work, 40 seconds rest for exercises like burpees, jumping jacks, and squats). Day 5: 40-minute swimming or biking. Day 6: Outdoor sports or a long hike (60 minutes). Day 7: Rest day or stretching for 15 minutes. Eating Plan: Breakfast: Oatmeal with almond milk, chia seeds, and fresh fruit. Lunch: Grilled chicken salad with mixed greens, avocado, and a light vinaigrette dressing. Snack: Whole grain crackers with cheese or hummus. Dinner: Stir-fry tofu or lean beef with brown rice and mixed vegetables. Hydration: 6-8 cups of water','Exercise Plan: Day 1: 20-minute jump rope session + 10 minutes of bodyweight strength exercises (push-ups, planks, squats). Day 2: 30-minute brisk walk or cycling. Day 3: Rest or 15-minute yoga/stretching. Day 4: 30-minute strength training (bodyweight or light weights) focusing on legs and core. Day 5: 25-minute interval running (30 seconds sprint, 1-minute walk) + 10 minutes of core exercises. Day 6: Fun outdoor activity (basketball, tennis, or soccer) for 45 minutes. Day 7: Rest day or light stretching for 15-20 minutes. Eating Plan: Breakfast: Smoothie with spinach, banana, almond milk, and protein powder (optional). Lunch: Whole grain wrap with grilled chicken, veggies, and hummus. Snack: A handful of almonds or yogurt with honey. Dinner: Grilled turkey burger with whole grain bun, side of sweet potato fries, and a salad. Hydration: 7-9 cups of water daily','Exercise Plan: Day 1: 30-minute light jog or cycling. Day 2: 25-minute HIIT session (jump squats, mountain climbers, and burpees). Day 3: Rest or 15 minutes of stretching/yoga. Day 4: 40-minute brisk walk or swimming. Day 5: 20-minute interval training (30 seconds sprint, 1-minute walk) + 10-minute ab exercises. Day 6: Fun outdoor activity (sports or a long hike) for 45-60 minutes. Day 7: Active recovery day (light stretching for 15-20 minutes or gentle yoga). Eating Plan: Breakfast: Whole grain toast with peanut butter and sliced bananas. Lunch: Quinoa salad with chickpeas, cucumbers, and feta cheese. Snack: Sliced vegetables with hummus or guacamole. Dinner: Baked fish with steamed vegetables and brown rice. Hydration: 7-9 cups of water daily']
exercise_obese_adult = ['Exercise Plan: Day 1: 30-minute brisk walk + 20-minute full-body strength training (push-ups, squats, lunges). Day 2: 30-minute moderate cycling or stationary bike + 10-minute core workout (planks, crunches). Day 3: Rest day or 20-minute light stretching/yoga. Day 4: 30-minute HIIT session (burpees, jumping jacks, mountain climbers) + 10 minutes of bodyweight strength exercises. Day 5: 40-minute brisk walking or swimming. Day 6: 60-minute outdoor sports (basketball, tennis, or hiking). Day 7: Rest day or 20-minute stretching. Eating Plan: Breakfast: Oatmeal with almond milk, chia seeds, and fresh berries. Lunch: Grilled chicken or tofu salad with mixed greens, quinoa, and olive oil dressing. Snack: A handful of almonds or a small apple with peanut butter. Dinner: Baked salmon or lean turkey with roasted vegetables and quinoa. Hydration: 8-10 cups of water daily','Exercise Plan: Day 1: 40-minute brisk walk or light jog + 15-minute core workout (planks, leg raises, mountain climbers). Day 2: 30-minute moderate cycling or swimming. Day 3: Rest day or 20-minute yoga/stretching. Day 4: 30-minute interval running (1-minute sprint, 2-minute walk) + 15-minute ab exercises. Day 5: 30-minute full-body strength training (dumbbells or bodyweight). Day 6: 45-minute outdoor activity (hiking, tennis, or cycling). Day 7: Rest or 20-minute yoga/stretching. Eating Plan: Breakfast: Greek yogurt with mixed berries, honey, and a handful of granola. Lunch: Grilled chicken with whole grain pasta, spinach, and a light olive oil dressing. Snack: Sliced cucumbers and carrots with hummus. Dinner: Stir-fry with lean beef, brown rice, and mixed vegetables. Hydration: 8-10 cups of water daily','Exercise Plan: Day 1: 30-minute brisk walk or light jog + 20-minute bodyweight exercises (push-ups, lunges, squats). Day 2: 30-minute moderate cycling or elliptical machine + 15 minutes of core work (planks, crunches). Day 3: Rest day or 20-minute yoga/stretching. Day 4: 30-minute strength training (weights or resistance bands) focusing on upper and lower body. Day 5: 30-minute HIIT session (jump squats, burpees, jumping jacks). Day 6: 45-minute outdoor sports (soccer, basketball, or hiking). Day 7: Rest day or 15 minutes of stretching/yoga. Eating Plan: Breakfast: Smoothie with banana, almond milk, spinach, and protein powder (optional). Lunch: Whole grain wrap with turkey, avocado, and mixed vegetables. Snack: A handful of nuts or a small handful of trail mix. Dinner: Grilled fish with quinoa and steamed broccoli. Hydration: 8-10 cups of water daily','Exercise Plan: Day 1: 30-minute power walk or light jog + 15-minute functional movements (jump squats, push-ups, lunges). Day 2: 30-minute HIIT session (burpees, mountain climbers, high knees). Day 3: Rest or light yoga/stretching for 20 minutes. Day 4: 25-minute interval training (1-minute sprint, 1-minute walk). Day 5: 30-minute strength workout focusing on core and lower body (squats, leg raises, planks). Day 6: 60-minute outdoor activity (swimming, cycling, or hiking). Day 7: Rest day or light stretching for 15-20 minutes. Eating Plan: Breakfast: Whole grain toast with avocado and scrambled eggs. Lunch: Tuna or chicken salad with mixed greens and a light vinaigrette. Snack: Sliced veggies with hummus or a boiled egg. Dinner: Stir-fry tofu or chicken with brown rice and veggies. Hydration: 8-10 cups of water daily','Exercise Plan: Day 1: 40-minute brisk walk or light jog. Day 2: 30-minute moderate cycling or stationary bike + 10 minutes of core exercises (crunches, planks). Day 3: Rest or 20-minute yoga/stretching. Day 4: 30-minute moderate jogging or brisk walking + 10-minute core workout. Day 5: 30-minute strength workout (upper and lower body) using bodyweight or light weights. Day 6: 60-minute outdoor sports (tennis, soccer, or hiking). Day 7: Rest or light stretching for 15-20 minutes. Eating Plan: Breakfast: Smoothie bowl with spinach, banana, almond milk, chia seeds, and a handful of granola. Lunch: Quinoa salad with grilled chicken or chickpeas, cucumbers, and light vinaigrette. Snack: Apple slices with almond butter or a handful of nuts. Dinner: Grilled turkey burger with sweet potatoes and roasted vegetables. Hydration: 8-10 cups of water daily']
exercise_overweight_adult = ['Exercise Plan: Day 1: 30-minute brisk walk or light jog + 20-minute strength training (push-ups, squats, lunges). Day 2: 30-minute moderate cycling or stationary bike + 15-minute core workout (planks, leg raises). Day 3: Rest or 20-minute light stretching/yoga. Day 4: 30-minute HIIT session (burpees, jumping jacks, mountain climbers) + 10-minute ab exercises. Day 5: 40-minute brisk walk or light jogging. Day 6: 45-minute outdoor sports (basketball, tennis, or hiking). Day 7: Rest day or 20-minute yoga/stretching. Eating Plan: Breakfast: Oatmeal with almond milk, chia seeds, and fresh berries. Lunch: Grilled chicken or tofu salad with mixed greens, quinoa, and olive oil dressing. Snack: A small handful of nuts or sliced apple with peanut butter. Dinner: Baked salmon or lean turkey with steamed vegetables and quinoa. Hydration: 8-10 cups of water daily','Exercise Plan: Day 1: 30-minute brisk walk + 15-minute core workout (planks, crunches, leg raises). Day 2: 30-minute moderate cycling or swimming. Day 3: Rest or 20-minute stretching/yoga. Day 4: 30-minute interval running (1-minute sprint, 2-minute walk) + 15-minute core workout. Day 5: 30-minute full-body strength training (dumbbells or bodyweight). Day 6: 45-minute outdoor activity (hiking, tennis, or cycling). Day 7: Rest day or 20-minute yoga/stretching. Eating Plan: Breakfast: Greek yogurt with mixed berries, honey, and a handful of granola. Lunch: Grilled chicken with whole grain pasta, spinach, and a light olive oil dressing. Snack: A handful of mixed nuts or carrot sticks with hummus. Dinner: Stir-fried lean beef, brown rice, and mixed vegetables. Hydration: 8-10 cups of water daily','Exercise Plan: Day 1: 25-minute brisk walk or light jogging + 20-minute bodyweight exercises (push-ups, lunges, squats). Day 2: 30-minute moderate cycling or elliptical + 10-minute core workout (planks, Russian twists). Day 3: Rest day or 20-minute yoga/stretching. Day 4: 30-minute strength training (weights or resistance bands) focusing on upper and lower body. Day 5: 30-minute HIIT session (jump squats, burpees, jumping jacks). Day 6: 45-minute outdoor sports (soccer, basketball, or hiking). Day 7: Rest day or 15 minutes of light stretching. Eating Plan: Breakfast: Smoothie with banana, almond milk, spinach, and protein powder (optional). Lunch: Turkey or chickpea wrap with whole grain tortilla, spinach, and avocado. Snack: A handful of almonds or a boiled egg. Dinner: Grilled fish with quinoa and steamed broccoli. Hydration: 8-10 cups of water daily','Exercise Plan: Day 1: 30-minute power walk or light jog + 15-minute functional movements (jump squats, push-ups, lunges). Day 2: 30-minute HIIT session (burpees, mountain climbers, high knees). Day 3: Rest or light yoga/stretching for 20 minutes. Day 4: 25-minute interval training (1-minute sprint, 1-minute walk). Day 5: 30-minute strength workout focusing on core and lower body (squats, planks, leg raises). Day 6: 60-minute outdoor activity (swimming, cycling, or hiking). Day 7: Rest or light stretching for 15-20 minutes. Eating Plan: Breakfast: Whole grain toast with avocado and scrambled eggs. Lunch: Tuna or chicken salad with mixed greens and light vinaigrette. Snack: Sliced cucumbers and carrots with hummus. Dinner: Stir-fry with lean chicken or tofu, brown rice, and veggies. Hydration: 8-10 cups of water daily','Exercise Plan: Day 1: 30-minute brisk walk or light jog + 15-minute flexibility exercises (stretching hamstrings, quads, and back). Day 2: 30-minute moderate cycling or stationary bike + 10-minute core workout (crunches, leg raises). Day 3: Rest day or light yoga/stretching for 20 minutes. Day 4: 30-minute interval running (1-minute sprint, 2-minute walk) + 15-minute strength workout. Day 5: 30-minute strength training (upper and lower body focus). Day 6: 60-minute outdoor sports (tennis, soccer, or hiking). Day 7: Rest day or light stretching for 15-20 minutes. Eating Plan: Breakfast: Smoothie with spinach, banana, almond milk, chia seeds, and a handful of granola. Lunch: Quinoa salad with grilled chicken, chickpeas, cucumbers, and light vinaigrette. Snack: Apple slices with almond butter or a handful of mixed nuts. Dinner: Grilled turkey burger with sweet potatoes and roasted vegetables. Hydration: 8-10 cups of water daily']
exercise_normal_adult = ['Exercise Plan: Day 1: 30-minute brisk walk or light jog + 20-minute strength training (push-ups, squats, lunges). Day 2: 30-minute moderate cycling or elliptical + 15-minute core workout (planks, Russian twists). Day 3: Rest or 20-minute light stretching/yoga. Day 4: 30-minute full-body strength training (bodyweight or light weights). Day 5: 30-minute HIIT session (burpees, jumping jacks, mountain climbers). Day 6: 45-minute outdoor activity (hiking, tennis, or basketball). Day 7: Rest or 20-minute stretching/yoga. Eating Plan: Breakfast: Oatmeal with chia seeds, almond milk, and berries. Lunch: Grilled chicken or tofu salad with mixed greens, quinoa, and olive oil dressing. Snack: Sliced apple with peanut butter or a small handful of almonds. Dinner: Grilled salmon or lean turkey with roasted vegetables and quinoa. Hydration: 8-10 cups of water daily','Exercise Plan: Day 1: 40-minute brisk walk or light jog + 10-minute core workout (planks, crunches). Day 2: 30-minute moderate cycling or swimming. Day 3: Rest day or 20-minute yoga/stretching. Day 4: 30-minute interval running (1-minute sprint, 2-minute walk) + 15-minute flexibility/stretching exercises. Day 5: 30-minute full-body strength training (bodyweight or dumbbells). Day 6: 60-minute outdoor activity (cycling, tennis, or hiking). Day 7: Rest or 20-minute yoga/stretching. Eating Plan: Breakfast: Smoothie with spinach, banana, almond milk, chia seeds, and protein powder (optional). Lunch: Grilled chicken with whole grain pasta, spinach, and light olive oil dressing. Snack: A handful of mixed nuts or cucumber slices with hummus. Dinner: Stir-fried lean beef or tofu with brown rice and mixed vegetables. Hydration: 8-10 cups of water daily','Exercise Plan: Day 1: 30-minute walk or light jog + 20-minute bodyweight strength workout (squats, lunges, push-ups). Day 2: 30-minute moderate cycling or elliptical + 15-minute core work (planks, mountain climbers). Day 3: Rest day or 20-minute yoga/stretching. Day 4: 30-minute strength training (upper and lower body using resistance bands or light weights). Day 5: 30-minute HIIT session (jump squats, burpees, jumping jacks). Day 6: 45-minute outdoor sports (basketball, soccer, or hiking). Day 7: Rest or light stretching/yoga for 15 minutes. Eating Plan: Breakfast: Whole grain toast with avocado and scrambled eggs. Lunch: Whole grain wrap with turkey or chickpeas, avocado, and mixed vegetables. Snack: Carrot sticks or sliced peppers with hummus. Dinner: Grilled fish with quinoa and roasted vegetables. Hydration: 8-10 cups of water daily','Exercise Plan: Day 1: 30-minute brisk walk + 15-minute HIIT (burpees, mountain climbers, high knees). Day 2: 30-minute moderate cycling or light jog + 10-minute core workout (planks, crunches). Day 3: Rest or 20-minute light stretching/yoga. Day 4: 25-minute interval running (1-minute sprint, 1-minute walk) + 10-minute core and leg workout. Day 5: 30-minute functional strength workout (push-ups, lunges, planks). Day 6: 45-minute outdoor activity (hiking, tennis, or soccer). Day 7: Rest day or light stretching for 15-20 minutes. Eating Plan: Breakfast: Smoothie with spinach, banana, protein powder (optional), almond milk, and chia seeds. Lunch: Quinoa salad with grilled chicken, cucumbers, and a light vinaigrette. Snack: A handful of almonds or apple slices with almond butter. Dinner: Stir-fried tofu or lean chicken with brown rice and steamed broccoli. Hydration: 8-10 cups of water daily','Exercise Plan: Day 1: 40-minute brisk walk or light jog + 15-minute flexibility training (yoga or dynamic stretching). Day 2: 30-minute moderate cycling or swimming + 10-minute core workout (leg raises, Russian twists). Day 3: Rest day or light yoga/stretching for 20 minutes. Day 4: 30-minute strength training (upper and lower body) using bodyweight or light dumbbells. Day 5: 30-minute HIIT session (burpees, jump squats, jumping jacks). Day 6: 45-minute outdoor activity (tennis, cycling, or hiking). Day 7: Rest or light stretching/yoga for 15-20 minutes. Eating Plan: Breakfast: Smoothie bowl with spinach, banana, almond milk, chia seeds, and a handful of granola. Lunch: Turkey burger on whole wheat bun with mixed greens and sweet potato fries. Snack: A boiled egg or cucumber slices with hummus. Dinner: Grilled lean beef or tofu with quinoa and roasted vegetables. Hydration: 8-10 cups of water daily']
exercise_underweight_adult = ['Exercise Plan: Day 1: 30-minute brisk walk or light jogging + 20-minute full-body strength training (push-ups, squats, lunges). Day 2: 25-minute moderate cycling or stationary bike + 10-minute core workout (planks, crunches). Day 3: Rest day or 20-minute yoga/stretching routine. Day 4: 30-minute strength training using weights or resistance bands (focus on upper body). Day 5: 40-minute light cardio (swimming, jogging, or brisk walking). Day 6: 60-minute outdoor activity (hiking, basketball, or tennis). Day 7: Rest day or 15-minute stretching/yoga. Eating Plan: Breakfast: Scrambled eggs with avocado and whole grain toast. Lunch: Grilled chicken or tofu salad with mixed greens, quinoa, and olive oil dressing. Snack: Greek yogurt with honey and almonds. Dinner: Baked salmon or lean beef with brown rice and steamed vegetables. Hydration: 7-9 cups of water daily','Exercise Plan: Day 1: 30-minute cycling + 15-minute ab exercises (planks, leg raises, mountain climbers). Day 2: 20-minute interval running (1-minute sprint, 2-minute walk) + 10 minutes of stretching. Day 3: 30-minute full-body strength workout (focus on arms, legs, and core). Day 4: Rest day or 20-minute yoga/stretching. Day 5: 30-minute moderate swimming or brisk walking. Day 6: 60-minute outdoor sports (soccer, basketball, or cycling). Day 7: Rest day or light stretching for 15-20 minutes. Eating Plan: Breakfast: Oatmeal with almond milk, chia seeds, and fresh fruit. Lunch: Whole grain pasta with grilled chicken, broccoli, and olive oil dressing. Snack: A handful of mixed nuts or a smoothie with spinach, banana, and almond milk. Dinner: Grilled chicken or fish with sweet potatoes and steamed vegetables. Hydration: 7-9 cups of water daily','Exercise Plan: Day 1: 25-minute brisk walk or light jogging + 20-minute bodyweight exercises (push-ups, squats, lunges). Day 2: 30-minute strength training (upper body focus) using dumbbells or resistance bands. Day 3: Rest day or 20-minute stretching/yoga. Day 4: 25-minute interval training (alternating between sprinting and walking). Day 5: 30-minute strength training (lower body focus) + 10-minute core exercises (planks, Russian twists). Day 6: 45-minute outdoor sports (basketball, tennis, or hiking). Day 7: Rest day or 15 minutes of light stretching. Eating Plan: Breakfast: Smoothie with banana, almond milk, peanut butter, and protein powder (optional). Lunch: Tuna or chicken salad wrap with whole grain tortillas and veggies. Snack: Hummus with veggie sticks or whole grain crackers. Dinner: Stir-fry with lean beef, tofu, or chicken, brown rice, and mixed vegetables. Hydration: 7-9 cups of water daily','Exercise Plan: Day 1: 20-minute jump rope session + 15-minute core workout (planks, crunches, leg raises). Day 2: 30-minute HIIT session (high-intensity interval training) with exercises like burpees, jumping jacks, and squats. Day 3: Rest or 20-minute yoga/stretching. Day 4: 25-minute moderate running or brisk walking. Day 5: 30-minute full-body strength workout (bodyweight or weights) + 10 minutes of core exercises. Day 6: Fun outdoor activity (soccer, basketball, or tennis) for 45-60 minutes. Day 7: Rest or 15 minutes of stretching. Eating Plan: Breakfast: Greek yogurt with mixed berries, honey, and granola. Lunch: Grilled chicken wrap with avocado, spinach, and hummus on whole grain tortilla. Snack: Whole grain crackers with cheese or a smoothie with almond milk, spinach, and chia seeds. Dinner: Grilled fish or chicken with quinoa and steamed veggies. Hydration: 7-9 cups of water daily','Exercise Plan: Day 1: 30-minute light jogging or cycling + 15-minute stretching routine (focus on hamstrings, quads, back). Day 2: 20-minute moderate jog or power walk + 10 minutes of core exercises (sit-ups, Russian twists, side planks). Day 3: 25-minute strength training (focus on legs and core) + 15-minute stretching or yoga. Day 4: Rest day or light stretching (15 minutes). Day 5: 40-minute swimming or hiking. Day 6: 60-minute outdoor sports (tennis, basketball, or hiking). Day 7: Rest day or 15-minute flexibility/stretching session. Eating Plan: Breakfast: Whole grain toast with avocado and a boiled egg. Lunch: Quinoa salad with chickpeas, cucumbers, feta cheese, and a light dressing. Snack: Carrot sticks with hummus or a protein shake. Dinner: Grilled turkey burger with whole grain bun, sweet potato fries, and a side salad. Hydration: 7-9 cups of water daily']
st.set_page_config(page_title="Welcome")
st.title("Your Specialized Exercise Plans Are Here!!")
st.subheader("Come and fill up this form to know what exercise plan works for you.")
with st.form(key='know_more_form'):
  st.header("This is a form to get to know more about you!")
  gender = st.selectbox("What is your gender?",["Female","Male"])
  age = st.slider("Which year are you born?",1944,2011)
  height = st.number_input("What is your height? (in meteres)",0.00,)
  weight = st.number_input("What is your weight? (in kilograms)",0.00,)
  st.form_submit_button("Submit")
height = height * height
try:
  bmi = weight / height
except ZeroDivisionError:
  st.write("Please give a valid number")
else:
  if bmi >= 40.0:
    st.write("You are obese")
    if age >= 2005:
      plans = st.selectbox("Select an exercise plan to view",("Plan 1","Plan 2","Plan 3"))
      if plans == 'Plan 1':
        st.write(rd.choice(exercise_obese_teens))
      elif plans == 'Plan 2':
        st.write(rd.choice(exercise_obese_teens))
      elif plans == 'Plan 3':
        st.write(rd.choice(exercise_obese_teens))
      else:
        st.write("Ok,I seee that you do not want to exercise")
    elif age >= 1975:
      plans = st.selectbox("Select an exercise plan to view",("Plan 1","Plan 2","Plan 3"))
      if plans == 'Plan 1':
        st.write(rd.choice(exercise_obese_adult))
      elif plans == 'Plan 2':
        st.write(rd.choice(exercise_obese_adult))
      elif plans == 'Plan 3':
        st.write(rd.choice(exercise_obese_adult))
      else:
        st.write("Ok,I seee that you do not want to exercise")
    else:
      plans = st.selectbox("Select an exercise plan to view",("Plan 1","Plan 2","Plan 3"))
      if plans == 'Plan 1':
        st.write(rd.choice(exercise_obese_teens))
      elif plans == 'Plan 2':
        st.write(rd.choice(exercise_obese_adult))
      elif plans == 'Plan 3':
        st.write(rd.choice(exercise_obese_teens))
      else:
        st.write("Ok,I seee that you do not want to exercise")  
  elif bmi >= 25.0:
    st.write("You are overweight")
    plans = st.selectbox("Select an exercise plan to view",("Plan 1","Plan 2","Plan 3"))
    if age >= 2005:
      if plans == 'Plan 1':
        st.write(rd.choice(exercise_overweight_teens))
      elif plans == 'Plan 2':
        st.write(rd.choice(exercise_overweight_teens))
      elif plans == 'Plan 3':
        st.write(rd.choice(exercise_overweight_teens))
      else:
        st.write("Ok,I seee that you do not want to exercise")
    elif age >= 1975:
      if plans == 'Plan 1':
        st.write(rd.choice(exercise_overweight_adult))
      elif plans == 'Plan 2':
        st.write(rd.choice(exercise_overweight_adult))
      elif plans == 'Plan 3':
        st.write(rd.choice(exercise_overweight_adult))
      else:
        st.write("Ok,I seee that you do not want to exercise")
    else:      
      if plans == 'Plan 1':
        st.write(rd.choice(exercise_overweight_adult))
      elif plans == 'Plan 2':
        st.write(rd.choice(exercise_overweight_teens))
      elif plans == 'Plan 3':
        st.write(rd.choice(exercise_overweight_adult))
      else:
        st.write("Ok,I seee that you do not want to exercise")
  elif bmi >=18.5:
    st.write("You are normal")
    if age >= 2005:
      plans = st.selectbox("Select an exercise plan to view",("Plan 1","Plan 2","Plan 3"))
      if plans == 'Plan 1':
        st.write(rd.choice(exercise_normal_teens))
      elif plans == 'Plan 2':
        st.write(rd.choice(exercise_normal_teens))
      elif plans == 'Plan 3':
        st.write(rd.choice(exercise_normal_teens))
      else:
        st.write("Ok,I seee that you do not want to exercise")
    elif age >= 1975:      
      plans = st.selectbox("Select an exercise plan to view",("Plan 1","Plan 2","Plan 3"))
      if plans == 'Plan 1':
        st.write(rd.choice(exercise_normal_adult))
      elif plans == 'Plan 2':
        st.write(rd.choice(exercise_normal_adult))
      elif plans == 'Plan 3':
        st.write(rd.choice(exercise_normal_adult))
      else:
        st.write("Ok,I seee that you do not want to exercise")
    else:      
      plans = st.selectbox("Select an exercise plan to view",("Plan 1","Plan 2","Plan 3"))
      if plans == 'Plan 1':
        st.write(rd.choice(exercise_normal_teens))
      elif plans == 'Plan 2':
        st.write(rd.choice(exercise_normal_teens))
      elif plans == 'Plan 3':
        st.write(rd.choice(exercise_normal_teens))
      else:
        st.write("Ok,I seee that you do not want to exercise")
  else:
    st.write("You are underweight")
    if age >= 2005:
      plans = st.selectbox("Select an exercise plan to view",("Plan 1","Plan 2","Plan 3"))
      if plans == 'Plan 1':
        st.write(rd.choice(exercise_underweight_teens))
      elif plans == 'Plan 2':
        st.write(rd.choice(exercisee_underweight_teens))
      elif plans == 'Plan 3':
        st.write(rd.choice(exercisee_underweight_teens))
      else:
        st.write("Ok,I seee that you do not want to exercise")
    elif age >= 1975:      
      plans = st.selectbox("Select an exercise plan to view",("Plan 1","Plan 2","Plan 3"))
      if plans == 'Plan 1':
        st.write(rd.choice(exercise_underweight_adult))
      elif plans == 'Plan 2':
        st.write(rd.choice(exercise_underweight_adult))
      elif plans == 'Plan 3':
        st.write(rd.choice(exercise_underweight_adult))
      else:
        st.write("Ok,I seee that you do not want to exercise")
    else:      
      plans = st.selectbox("Select an exercise plan to view",("Plan 1","Plan 2","Plan 3"))
      if plans == 'Plan 1':
        st.write("You should start eating more man")
      elif plans == 'Plan 2':
        st.write("You should start eating more man")
      elif plans == 'Plan 3':
        st.write("You should start eating more man")
      else:
        st.write("Ok,I seee that you do not want to exercise")
