import tkinter as tk
import tkinter.messagebox
from tkinter import ttk

from pygame import mixer
from PIL import Image, ImageTk

global current_page_number
global current_page
global selected_kana
mixer.init()


def main_menu(root):
    global current_page_number
    global current_page
    current_page_number = 0
    current_page = 'main_menu'

    learn_btn_image = tk.PhotoImage(file="resources/imgs/button_learn.png")
    practice_btn_image = tk.PhotoImage(file="resources/imgs/button_practice.png")
    sprint_btn_image = tk.PhotoImage(file="resources/imgs/button_sprint.png")
    time_trial_btn_image = tk.PhotoImage(file="resources/imgs/button_time-trial.png")
    settings_btn_image = tk.PhotoImage(file="resources/imgs/button_settings.png")

    canvas = tk.Canvas(root, width=450, height=700, background="#bdd1ff", borderwidth=0, highlightthickness=0)
    canvas.grid(columnspan=3, rowspan=6)

    # logo

    logo = Image.open('resources/imgs/dogaku_logo.png')
    logo = ImageTk.PhotoImage(logo)
    logo_label = tk.Label(image=logo, borderwidth=0, highlightthickness=0, height=200)
    logo_label.image = logo
    logo_label.grid(column=2, row=0)

    learn_btn = tk.Button(root, command=lambda: change_page(root, 'kana_selection'), border=0, borderwidth=0, background="#bdd1ff", activebackground="#bdd1ff")
    learn_btn.config(image=learn_btn_image)
    learn_btn.image = learn_btn_image
    learn_btn.grid(column=2, row=1)

    practice_btn = tk.Button(root, command=lambda: show_error_msg(root), border=0, borderwidth=0, background="#bdd1ff", activebackground="#bdd1ff")
    practice_btn.config(image=practice_btn_image)
    practice_btn.image = practice_btn_image
    practice_btn.grid(column=2, row=2)

    sprint_btn = tk.Button(root, command=lambda: show_error_msg(root), border=0, borderwidth=0, background="#bdd1ff", activebackground="#bdd1ff")
    sprint_btn.config(image=sprint_btn_image)
    sprint_btn.image = sprint_btn_image
    sprint_btn.grid(column=2, row=3)

    time_trial_btn = tk.Button(root, command=lambda: show_error_msg(root), border=0, borderwidth=0, background="#bdd1ff", activebackground="#bdd1ff")
    time_trial_btn.config(image=time_trial_btn_image)
    time_trial_btn.image = time_trial_btn_image
    time_trial_btn.grid(column=2, row=4)

    settings_btn = tk.Button(root, command=lambda: show_error_msg(root), border=0, borderwidth=0, background="#bdd1ff", activebackground="#bdd1ff")
    settings_btn.config(image=settings_btn_image)
    settings_btn.image = settings_btn_image
    settings_btn.grid(column=2, row=5)

    spacer_canvas = tk.Canvas(root, width=600, height=130, background="#bdd1ff", borderwidth=0, highlightthickness=0)
    spacer_canvas.grid(columnspan=3)


def learn_menu(root):
    global current_page
    global selected_kana
    current_page = 'learn_menu'

    sound_btn_image = tk.PhotoImage(file="resources/imgs/button_listen.png")
    sound_btn = tk.Button(root, border=0, borderwidth=0, background="#bdd1ff", activebackground="#bdd1ff")
    sound_btn.config(image=sound_btn_image)
    sound_btn_image.image = sound_btn_image
    sound_btn.grid(column=2, row=1, pady=(0,20))

    exit_btn_image = tk.PhotoImage(file="resources/imgs/button_exit.png")
    exit_btn = tk.Button(root, command=lambda: change_page(root, 'main_menu'), border=0, borderwidth=0, background="#bdd1ff", activebackground="#bdd1ff")
    exit_btn.config(image=exit_btn_image)
    exit_btn_image.image = exit_btn_image
    exit_btn.grid(column=2, row=2, pady=(0,30))

    position_1_label = tk.Label(borderwidth=5, highlightthickness=0, background="#bdd1ff")
    position_1_label.grid(column=0, row=0, padx=(30, 0), pady=(30, 50))

    position_2_label = tk.Label(borderwidth=5, highlightthickness=0, background="#bdd1ff")
    position_2_label.grid(column=1, row=0, pady=(30, 50))

    position_3_label = tk.Label(borderwidth=5, highlightthickness=0, background="#bdd1ff")
    position_3_label.grid(column=2, row=0, pady=(30, 50))

    position_4_label = tk.Label(borderwidth=5, highlightthickness=0, background="#bdd1ff")
    position_4_label.grid(column=3, row=0, pady=(30, 50))

    position_5_label = tk.Label(borderwidth=5, highlightthickness=0, background="#bdd1ff")
    position_5_label.grid(column=4, row=0, padx=(0, 30), pady=(30, 50))

    if current_page_number == 0:
        sound_btn.configure(command=lambda: play_sound('aiueo'))
        if selected_kana == 'hiragana':
            position_1_image = tk.PhotoImage(file="resources/imgs/hiragana_a.png")
            position_1_label.configure(image=position_1_image)
            position_1_label.image = position_1_image

            position_2_image = tk.PhotoImage(file="resources/imgs/hiragana_i.png")
            position_2_label.configure(image=position_2_image)
            position_2_label.image = position_2_image

            position_3_image = tk.PhotoImage(file="resources/imgs/hiragana_u.png")
            position_3_label.configure(image=position_3_image)
            position_3_label.image = position_3_image

            position_4_image = tk.PhotoImage(file="resources/imgs/hiragana_e.png")
            position_4_label.configure(image=position_4_image)
            position_4_label.image = position_4_image

            position_5_image = tk.PhotoImage(file="resources/imgs/hiragana_o.png")
            position_5_label.configure(image=position_5_image)
            position_5_label.image = position_5_image
        else:
            position_1_image = tk.PhotoImage(file="resources/imgs/katakana_a.png")
            position_1_label.configure(image=position_1_image)
            position_1_label.image = position_1_image

            position_2_image = tk.PhotoImage(file="resources/imgs/katakana_i.png")
            position_2_label.configure(image=position_2_image)
            position_2_label.image = position_2_image

            position_3_image = tk.PhotoImage(file="resources/imgs/katakana_u.png")
            position_3_label.configure(image=position_3_image)
            position_3_label.image = position_3_image

            position_4_image = tk.PhotoImage(file="resources/imgs/katakana_e.png")
            position_4_label.configure(image=position_4_image)
            position_4_label.image = position_4_image

            position_5_image = tk.PhotoImage(file="resources/imgs/katakana_o.png")
            position_5_label.configure(image=position_5_image)
            position_5_label.image = position_5_image

        forward_btn_image = tk.PhotoImage(file="resources/imgs/next_page_button.png")
        forward_btn = tk.Button(root, command=lambda: increase_page_count(), border=0, borderwidth=0, background="#bdd1ff", activebackground="#bdd1ff")
        forward_btn.config(image=forward_btn_image)
        forward_btn_image.image = forward_btn_image
        forward_btn.grid(column=3, row=2, pady=(0, 30))

    elif current_page_number == 1:
        sound_btn.configure(command=lambda: play_sound('kakikukeko'))
        if selected_kana == 'hiragana':
            position_1_image = tk.PhotoImage(file="resources/imgs/hiragana_ka.png")
            position_1_label.configure(image=position_1_image)
            position_1_label.image = position_1_image

            position_2_image = tk.PhotoImage(file="resources/imgs/hiragana_ki.png")
            position_2_label.configure(image=position_2_image)
            position_2_label.image = position_2_image

            position_3_image = tk.PhotoImage(file="resources/imgs/hiragana_ku.png")
            position_3_label.configure(image=position_3_image)
            position_3_label.image = position_3_image

            position_4_image = tk.PhotoImage(file="resources/imgs/hiragana_ke.png")
            position_4_label.configure(image=position_4_image)
            position_4_label.image = position_4_image

            position_5_image = tk.PhotoImage(file="resources/imgs/hiragana_ko.png")
            position_5_label.configure(image=position_5_image)
            position_5_label.image = position_5_image
        else:
            position_1_image = tk.PhotoImage(file="resources/imgs/katakana_ka.png")
            position_1_label.configure(image=position_1_image)
            position_1_label.image = position_1_image

            position_2_image = tk.PhotoImage(file="resources/imgs/katakana_ki.png")
            position_2_label.configure(image=position_2_image)
            position_2_label.image = position_2_image

            position_3_image = tk.PhotoImage(file="resources/imgs/katakana_ku.png")
            position_3_label.configure(image=position_3_image)
            position_3_label.image = position_3_image

            position_4_image = tk.PhotoImage(file="resources/imgs/katakana_ke.png")
            position_4_label.configure(image=position_4_image)
            position_4_label.image = position_4_image

            position_5_image = tk.PhotoImage(file="resources/imgs/katakana_ko.png")
            position_5_label.configure(image=position_5_image)
            position_5_label.image = position_5_image

        back_btn_image = tk.PhotoImage(file="resources/imgs/last_page_button.png")
        back_btn = tk.Button(root, command=lambda: decrease_page_count(), border=0, borderwidth=0, background="#bdd1ff", activebackground="#bdd1ff")
        back_btn.config(image=back_btn_image)
        back_btn_image.image = back_btn_image
        back_btn.grid(column=1, row=2, pady=(0, 30))

        forward_btn_image = tk.PhotoImage(file="resources/imgs/next_page_button.png")
        forward_btn = tk.Button(root, command=lambda: increase_page_count(), border=0, borderwidth=0, background="#bdd1ff", activebackground="#bdd1ff")
        forward_btn.config(image=forward_btn_image)
        forward_btn_image.image = forward_btn_image
        forward_btn.grid(column=3, row=2, pady=(0, 30))

    elif current_page_number == 2:
        sound_btn.configure(command=lambda: play_sound('sashisuseso'))
        if selected_kana == 'hiragana':
            position_1_image = tk.PhotoImage(file="resources/imgs/hiragana_sa.png")
            position_1_label.configure(image=position_1_image)
            position_1_label.image = position_1_image

            position_2_image = tk.PhotoImage(file="resources/imgs/hiragana_shi.png")
            position_2_label.configure(image=position_2_image)
            position_2_label.image = position_2_image

            position_3_image = tk.PhotoImage(file="resources/imgs/hiragana_su.png")
            position_3_label.configure(image=position_3_image)
            position_3_label.image = position_3_image

            position_4_image = tk.PhotoImage(file="resources/imgs/hiragana_se.png")
            position_4_label.configure(image=position_4_image)
            position_4_label.image = position_4_image

            position_5_image = tk.PhotoImage(file="resources/imgs/hiragana_so.png")
            position_5_label.configure(image=position_5_image)
            position_5_label.image = position_5_image
        else:
            position_1_image = tk.PhotoImage(file="resources/imgs/katakana_sa.png")
            position_1_label.configure(image=position_1_image)
            position_1_label.image = position_1_image

            position_2_image = tk.PhotoImage(file="resources/imgs/katakana_shi.png")
            position_2_label.configure(image=position_2_image)
            position_2_label.image = position_2_image

            position_3_image = tk.PhotoImage(file="resources/imgs/katakana_su.png")
            position_3_label.configure(image=position_3_image)
            position_3_label.image = position_3_image

            position_4_image = tk.PhotoImage(file="resources/imgs/katakana_se.png")
            position_4_label.configure(image=position_4_image)
            position_4_label.image = position_4_image

            position_5_image = tk.PhotoImage(file="resources/imgs/katakana_so.png")
            position_5_label.configure(image=position_5_image)
            position_5_label.image = position_5_image
        back_btn_image = tk.PhotoImage(file="resources/imgs/last_page_button.png")
        back_btn = tk.Button(root, command=lambda: decrease_page_count(), border=0, borderwidth=0, background="#bdd1ff", activebackground="#bdd1ff")
        back_btn.config(image=back_btn_image)
        back_btn_image.image = back_btn_image
        back_btn.grid(column=1, row=2, pady=(0, 30))

        forward_btn_image = tk.PhotoImage(file="resources/imgs/next_page_button.png")
        forward_btn = tk.Button(root, command=lambda: increase_page_count(), border=0, borderwidth=0, background="#bdd1ff", activebackground="#bdd1ff")
        forward_btn.config(image=forward_btn_image)
        forward_btn_image.image = forward_btn_image
        forward_btn.grid(column=3, row=2, pady=(0, 30))

    elif current_page_number == 3:
        sound_btn.configure(command=lambda: play_sound('tachitsuteto'))
        if selected_kana == 'hiragana':
            position_1_image = tk.PhotoImage(file="resources/imgs/hiragana_ta.png")
            position_1_label.configure(image=position_1_image)
            position_1_label.image = position_1_image

            position_2_image = tk.PhotoImage(file="resources/imgs/hiragana_chi.png")
            position_2_label.configure(image=position_2_image)
            position_2_label.image = position_2_image

            position_3_image = tk.PhotoImage(file="resources/imgs/hiragana_tsu.png")
            position_3_label.configure(image=position_3_image)
            position_3_label.image = position_3_image

            position_4_image = tk.PhotoImage(file="resources/imgs/hiragana_te.png")
            position_4_label.configure(image=position_4_image)
            position_4_label.image = position_4_image

            position_5_image = tk.PhotoImage(file="resources/imgs/hiragana_to.png")
            position_5_label.configure(image=position_5_image)
            position_5_label.image = position_5_image
        else:
            position_1_image = tk.PhotoImage(file="resources/imgs/katakana_ta.png")
            position_1_label.configure(image=position_1_image)
            position_1_label.image = position_1_image

            position_2_image = tk.PhotoImage(file="resources/imgs/katakana_chi.png")
            position_2_label.configure(image=position_2_image)
            position_2_label.image = position_2_image

            position_3_image = tk.PhotoImage(file="resources/imgs/katakana_tsu.png")
            position_3_label.configure(image=position_3_image)
            position_3_label.image = position_3_image

            position_4_image = tk.PhotoImage(file="resources/imgs/katakana_te.png")
            position_4_label.configure(image=position_4_image)
            position_4_label.image = position_4_image

            position_5_image = tk.PhotoImage(file="resources/imgs/katakana_to.png")
            position_5_label.configure(image=position_5_image)
            position_5_label.image = position_5_image
        back_btn_image = tk.PhotoImage(file="resources/imgs/last_page_button.png")
        back_btn = tk.Button(root, command=lambda: decrease_page_count(), border=0, borderwidth=0, background="#bdd1ff", activebackground="#bdd1ff")
        back_btn.config(image=back_btn_image)
        back_btn_image.image = back_btn_image
        back_btn.grid(column=1, row=2, pady=(0, 30))

        forward_btn_image = tk.PhotoImage(file="resources/imgs/next_page_button.png")
        forward_btn = tk.Button(root, command=lambda: increase_page_count(), border=0, borderwidth=0, background="#bdd1ff", activebackground="#bdd1ff")
        forward_btn.config(image=forward_btn_image)
        forward_btn_image.image = forward_btn_image
        forward_btn.grid(column=3, row=2, pady=(0, 30))

    elif current_page_number == 4:
        sound_btn.configure(command=lambda: play_sound('naninuneno'))
        if selected_kana == 'hiragana':
            position_1_image = tk.PhotoImage(file="resources/imgs/hiragana_na.png")
            position_1_label.configure(image=position_1_image)
            position_1_label.image = position_1_image

            position_2_image = tk.PhotoImage(file="resources/imgs/hiragana_ni.png")
            position_2_label.configure(image=position_2_image)
            position_2_label.image = position_2_image

            position_3_image = tk.PhotoImage(file="resources/imgs/hiragana_nu.png")
            position_3_label.configure(image=position_3_image)
            position_3_label.image = position_3_image

            position_4_image = tk.PhotoImage(file="resources/imgs/hiragana_ne.png")
            position_4_label.configure(image=position_4_image)
            position_4_label.image = position_4_image

            position_5_image = tk.PhotoImage(file="resources/imgs/hiragana_no.png")
            position_5_label.configure(image=position_5_image)
            position_5_label.image = position_5_image
        else:
            position_1_image = tk.PhotoImage(file="resources/imgs/katakana_na.png")
            position_1_label.configure(image=position_1_image)
            position_1_label.image = position_1_image

            position_2_image = tk.PhotoImage(file="resources/imgs/katakana_ni.png")
            position_2_label.configure(image=position_2_image)
            position_2_label.image = position_2_image

            position_3_image = tk.PhotoImage(file="resources/imgs/katakana_nu.png")
            position_3_label.configure(image=position_3_image)
            position_3_label.image = position_3_image

            position_4_image = tk.PhotoImage(file="resources/imgs/katakana_ne.png")
            position_4_label.configure(image=position_4_image)
            position_4_label.image = position_4_image

            position_5_image = tk.PhotoImage(file="resources/imgs/katakana_no.png")
            position_5_label.configure(image=position_5_image)
            position_5_label.image = position_5_image
        back_btn_image = tk.PhotoImage(file="resources/imgs/last_page_button.png")
        back_btn = tk.Button(root, command=lambda: decrease_page_count(), border=0, borderwidth=0, background="#bdd1ff", activebackground="#bdd1ff")
        back_btn.config(image=back_btn_image)
        back_btn_image.image = back_btn_image
        back_btn.grid(column=1, row=2, pady=(0, 30))

        forward_btn_image = tk.PhotoImage(file="resources/imgs/next_page_button.png")
        forward_btn = tk.Button(root, command=lambda: increase_page_count(), border=0, borderwidth=0, background="#bdd1ff", activebackground="#bdd1ff")
        forward_btn.config(image=forward_btn_image)
        forward_btn_image.image = forward_btn_image
        forward_btn.grid(column=3, row=2, pady=(0, 30))

    elif current_page_number == 5:
        sound_btn.configure(command=lambda: play_sound('hahifuheho'))
        if selected_kana == 'hiragana':
            position_1_image = tk.PhotoImage(file="resources/imgs/hiragana_ha.png")
            position_1_label.configure(image=position_1_image)
            position_1_label.image = position_1_image

            position_2_image = tk.PhotoImage(file="resources/imgs/hiragana_hi.png")
            position_2_label.configure(image=position_2_image)
            position_2_label.image = position_2_image

            position_3_image = tk.PhotoImage(file="resources/imgs/hiragana_fu.png")
            position_3_label.configure(image=position_3_image)
            position_3_label.image = position_3_image

            position_4_image = tk.PhotoImage(file="resources/imgs/hiragana_he.png")
            position_4_label.configure(image=position_4_image)
            position_4_label.image = position_4_image

            position_5_image = tk.PhotoImage(file="resources/imgs/hiragana_ho.png")
            position_5_label.configure(image=position_5_image)
            position_5_label.image = position_5_image
        else:
            position_1_image = tk.PhotoImage(file="resources/imgs/katakana_ha.png")
            position_1_label.configure(image=position_1_image)
            position_1_label.image = position_1_image

            position_2_image = tk.PhotoImage(file="resources/imgs/katakana_hi.png")
            position_2_label.configure(image=position_2_image)
            position_2_label.image = position_2_image

            position_3_image = tk.PhotoImage(file="resources/imgs/katakana_fu.png")
            position_3_label.configure(image=position_3_image)
            position_3_label.image = position_3_image

            position_4_image = tk.PhotoImage(file="resources/imgs/katakana_he.png")
            position_4_label.configure(image=position_4_image)
            position_4_label.image = position_4_image

            position_5_image = tk.PhotoImage(file="resources/imgs/katakana_ho.png")
            position_5_label.configure(image=position_5_image)
            position_5_label.image = position_5_image
        back_btn_image = tk.PhotoImage(file="resources/imgs/last_page_button.png")
        back_btn = tk.Button(root, command=lambda: decrease_page_count(), border=0, borderwidth=0, background="#bdd1ff", activebackground="#bdd1ff")
        back_btn.config(image=back_btn_image)
        back_btn_image.image = back_btn_image
        back_btn.grid(column=1, row=2, pady=(0, 30))

        forward_btn_image = tk.PhotoImage(file="resources/imgs/next_page_button.png")
        forward_btn = tk.Button(root, command=lambda: increase_page_count(), border=0, borderwidth=0, background="#bdd1ff", activebackground="#bdd1ff")
        forward_btn.config(image=forward_btn_image)
        forward_btn_image.image = forward_btn_image
        forward_btn.grid(column=3, row=2, pady=(0, 30))

    elif current_page_number == 6:
        sound_btn.configure(command=lambda: play_sound('mamimumemo'))
        if selected_kana == 'hiragana':
            position_1_image = tk.PhotoImage(file="resources/imgs/hiragana_ma.png")
            position_1_label.configure(image=position_1_image)
            position_1_label.image = position_1_image

            position_2_image = tk.PhotoImage(file="resources/imgs/hiragana_mi.png")
            position_2_label.configure(image=position_2_image)
            position_2_label.image = position_2_image

            position_3_image = tk.PhotoImage(file="resources/imgs/hiragana_mu.png")
            position_3_label.configure(image=position_3_image)
            position_3_label.image = position_3_image

            position_4_image = tk.PhotoImage(file="resources/imgs/hiragana_me.png")
            position_4_label.configure(image=position_4_image)
            position_4_label.image = position_4_image

            position_5_image = tk.PhotoImage(file="resources/imgs/hiragana_mo.png")
            position_5_label.configure(image=position_5_image)
            position_5_label.image = position_5_image
        else:
            position_1_image = tk.PhotoImage(file="resources/imgs/katakana_ma.png")
            position_1_label.configure(image=position_1_image)
            position_1_label.image = position_1_image

            position_2_image = tk.PhotoImage(file="resources/imgs/katakana_mi.png")
            position_2_label.configure(image=position_2_image)
            position_2_label.image = position_2_image

            position_3_image = tk.PhotoImage(file="resources/imgs/katakana_mu.png")
            position_3_label.configure(image=position_3_image)
            position_3_label.image = position_3_image

            position_4_image = tk.PhotoImage(file="resources/imgs/katakana_me.png")
            position_4_label.configure(image=position_4_image)
            position_4_label.image = position_4_image

            position_5_image = tk.PhotoImage(file="resources/imgs/katakana_mo.png")
            position_5_label.configure(image=position_5_image)
            position_5_label.image = position_5_image
        back_btn_image = tk.PhotoImage(file="resources/imgs/last_page_button.png")
        back_btn = tk.Button(root, command=lambda: decrease_page_count(), border=0, borderwidth=0, background="#bdd1ff", activebackground="#bdd1ff")
        back_btn.config(image=back_btn_image)
        back_btn_image.image = back_btn_image
        back_btn.grid(column=1, row=2, pady=(0, 30))

        forward_btn_image = tk.PhotoImage(file="resources/imgs/next_page_button.png")
        forward_btn = tk.Button(root, command=lambda: increase_page_count(), border=0, borderwidth=0, background="#bdd1ff", activebackground="#bdd1ff")
        forward_btn.config(image=forward_btn_image)
        forward_btn_image.image = forward_btn_image
        forward_btn.grid(column=3, row=2, pady=(0, 30))

    elif current_page_number == 7:
        sound_btn.configure(command=lambda: play_sound('yayuyo'))
        if selected_kana == 'hiragana':
            position_1_image = tk.PhotoImage(file="resources/imgs/hiragana_ya.png")
            position_1_label.configure(image=position_1_image)
            position_1_label.image = position_1_image

            position_2_image = tk.PhotoImage(file="resources/imgs/hiragana_spacer.png")
            position_2_label.configure(image=position_2_image)
            position_2_label.image = position_2_image

            position_3_image = tk.PhotoImage(file="resources/imgs/hiragana_yu.png")
            position_3_label.configure(image=position_3_image)
            position_3_label.image = position_3_image

            position_4_image = tk.PhotoImage(file="resources/imgs/hiragana_spacer.png")
            position_4_label.configure(image=position_4_image)
            position_4_label.image = position_4_image

            position_5_image = tk.PhotoImage(file="resources/imgs/hiragana_yo.png")
            position_5_label.configure(image=position_5_image)
            position_5_label.image = position_5_image
        else:
            position_1_image = tk.PhotoImage(file="resources/imgs/katakana_ya.png")
            position_1_label.configure(image=position_1_image)
            position_1_label.image = position_1_image

            position_2_image = tk.PhotoImage(file="resources/imgs/hiragana_spacer.png")
            position_2_label.configure(image=position_2_image)
            position_2_label.image = position_2_image

            position_3_image = tk.PhotoImage(file="resources/imgs/katakana_yu.png")
            position_3_label.configure(image=position_3_image)
            position_3_label.image = position_3_image

            position_4_image = tk.PhotoImage(file="resources/imgs/hiragana_spacer.png")
            position_4_label.configure(image=position_4_image)
            position_4_label.image = position_4_image

            position_5_image = tk.PhotoImage(file="resources/imgs/katakana_yo.png")
            position_5_label.configure(image=position_5_image)
            position_5_label.image = position_5_image
        back_btn_image = tk.PhotoImage(file="resources/imgs/last_page_button.png")
        back_btn = tk.Button(root, command=lambda: decrease_page_count(), border=0, borderwidth=0, background="#bdd1ff", activebackground="#bdd1ff")
        back_btn.config(image=back_btn_image)
        back_btn_image.image = back_btn_image
        back_btn.grid(column=1, row=2, pady=(0, 30))

        forward_btn_image = tk.PhotoImage(file="resources/imgs/next_page_button.png")
        forward_btn = tk.Button(root, command=lambda: increase_page_count(), border=0, borderwidth=0, background="#bdd1ff", activebackground="#bdd1ff")
        forward_btn.config(image=forward_btn_image)
        forward_btn_image.image = forward_btn_image
        forward_btn.grid(column=3, row=2, pady=(0, 30))

    elif current_page_number == 8:
        sound_btn.configure(command=lambda: play_sound('rarirurero'))
        if selected_kana == 'hiragana':
            position_1_image = tk.PhotoImage(file="resources/imgs/hiragana_ra.png")
            position_1_label.configure(image=position_1_image)
            position_1_label.image = position_1_image

            position_2_image = tk.PhotoImage(file="resources/imgs/hiragana_ri.png")
            position_2_label.configure(image=position_2_image)
            position_2_label.image = position_2_image

            position_3_image = tk.PhotoImage(file="resources/imgs/hiragana_ru.png")
            position_3_label.configure(image=position_3_image)
            position_3_label.image = position_3_image

            position_4_image = tk.PhotoImage(file="resources/imgs/hiragana_re.png")
            position_4_label.configure(image=position_4_image)
            position_4_label.image = position_4_image

            position_5_image = tk.PhotoImage(file="resources/imgs/hiragana_ro.png")
            position_5_label.configure(image=position_5_image)
            position_5_label.image = position_5_image
        else:
            position_1_image = tk.PhotoImage(file="resources/imgs/katakana_ra.png")
            position_1_label.configure(image=position_1_image)
            position_1_label.image = position_1_image

            position_2_image = tk.PhotoImage(file="resources/imgs/katakana_ri.png")
            position_2_label.configure(image=position_2_image)
            position_2_label.image = position_2_image

            position_3_image = tk.PhotoImage(file="resources/imgs/katakana_ru.png")
            position_3_label.configure(image=position_3_image)
            position_3_label.image = position_3_image

            position_4_image = tk.PhotoImage(file="resources/imgs/katakana_re.png")
            position_4_label.configure(image=position_4_image)
            position_4_label.image = position_4_image

            position_5_image = tk.PhotoImage(file="resources/imgs/katakana_ro.png")
            position_5_label.configure(image=position_5_image)
            position_5_label.image = position_5_image
        back_btn_image = tk.PhotoImage(file="resources/imgs/last_page_button.png")
        back_btn = tk.Button(root, command=lambda: decrease_page_count(), border=0, borderwidth=0, background="#bdd1ff", activebackground="#bdd1ff")
        back_btn.config(image=back_btn_image)
        back_btn_image.image = back_btn_image
        back_btn.grid(column=1, row=2, pady=(0, 30))

        forward_btn_image = tk.PhotoImage(file="resources/imgs/next_page_button.png")
        forward_btn = tk.Button(root, command=lambda: increase_page_count(), border=0, borderwidth=0, background="#bdd1ff", activebackground="#bdd1ff")
        forward_btn.config(image=forward_btn_image)
        forward_btn_image.image = forward_btn_image
        forward_btn.grid(column=3, row=2, pady=(0, 30))

    elif current_page_number == 9:
        sound_btn.configure(command=lambda: play_sound('waon'))
        if selected_kana == 'hiragana':
            position_1_image = tk.PhotoImage(file="resources/imgs/hiragana_wa.png")
            position_1_label.configure(image=position_1_image)
            position_1_label.image = position_1_image

            position_2_image = tk.PhotoImage(file="resources/imgs/hiragana_spacer.png")
            position_2_label.configure(image=position_2_image)
            position_2_label.image = position_2_image

            position_3_image = tk.PhotoImage(file="resources/imgs/hiragana_wo.png")
            position_3_label.configure(image=position_3_image)
            position_3_label.image = position_3_image

            position_4_image = tk.PhotoImage(file="resources/imgs/hiragana_spacer.png")
            position_4_label.configure(image=position_4_image)
            position_4_label.image = position_4_image

            position_5_image = tk.PhotoImage(file="resources/imgs/hiragana_n.png")
            position_5_label.configure(image=position_5_image)
            position_5_label.image = position_5_image
        else:
            position_1_image = tk.PhotoImage(file="resources/imgs/katakana_wa.png")
            position_1_label.configure(image=position_1_image)
            position_1_label.image = position_1_image

            position_2_image = tk.PhotoImage(file="resources/imgs/hiragana_spacer.png")
            position_2_label.configure(image=position_2_image)
            position_2_label.image = position_2_image

            position_3_image = tk.PhotoImage(file="resources/imgs/katakana_wo.png")
            position_3_label.configure(image=position_3_image)
            position_3_label.image = position_3_image

            position_4_image = tk.PhotoImage(file="resources/imgs/hiragana_spacer.png")
            position_4_label.configure(image=position_4_image)
            position_4_label.image = position_4_image

            position_5_image = tk.PhotoImage(file="resources/imgs/katakana_n.png")
            position_5_label.configure(image=position_5_image)
            position_5_label.image = position_5_image
        back_btn_image = tk.PhotoImage(file="resources/imgs/last_page_button.png")
        back_btn = tk.Button(root, command=lambda: decrease_page_count(), border=0, borderwidth=0, background="#bdd1ff", activebackground="#bdd1ff")
        back_btn.config(image=back_btn_image)
        back_btn_image.image = back_btn_image
        back_btn.grid(column=1, row=2, pady=(0, 30))


def show_error_msg(root):
    tkinter.messagebox.showwarning("DOGAKU", message="This feature is still in work. Check github.com/tellemiller for regular updates.")


def kana_selection_menu(root):
    hiragana_btn_image = tk.PhotoImage(file="resources/imgs/button_hiragana.png")
    hiragana_btn = tk.Button(root, command=lambda: set_learning_mode("hiragana"), border=0, borderwidth=0, background="#bdd1ff", activebackground="#bdd1ff")
    hiragana_btn.config(image=hiragana_btn_image)
    hiragana_btn_image.image = hiragana_btn_image
    hiragana_btn.grid(column=0, row=0, pady=(60, 15), padx=100)

    katakana_btn_image = tk.PhotoImage(file="resources/imgs/button_katakana.png")
    katakana_btn = tk.Button(root, command=lambda: set_learning_mode("katakana"), border=0, borderwidth=0, background="#bdd1ff", activebackground="#bdd1ff")
    katakana_btn.config(image=katakana_btn_image)
    katakana_btn_image.image = katakana_btn_image
    katakana_btn.grid(column=0, row=1, pady=(0, 90))

    exit_btn_image = tk.PhotoImage(file="resources/imgs/button_exit.png")
    exit_btn = tk.Button(root, command=lambda: change_page(root, 'main_menu'), border=0, borderwidth=0, background="#bdd1ff", activebackground="#bdd1ff")
    exit_btn.config(image=exit_btn_image)
    exit_btn_image.image = exit_btn_image
    exit_btn.grid(column=0, row=2, pady=(0, 60))


def practice(root):
    def check_answer(event):
        print(answer.get())

    global current_page
    current_page = 'practice'
    answer = tk.StringVar()

    position_1_label = tk.Label(borderwidth=5, highlightthickness=0, background="#bdd1ff")
    position_1_label.grid(column=0, row=0, padx=(30, 0), pady=(30,0))
    position_1_image = tk.PhotoImage(file="resources/imgs/hiragana_a_input.png")
    position_1_label.configure(image=position_1_image)
    position_1_label.image = position_1_image

    position_2_label = tk.Label(borderwidth=5, highlightthickness=0, background="#bdd1ff")
    position_2_label.grid(column=2, row=0, padx=(0, 70), pady=(30,0))
    position_2_image = tk.PhotoImage(file="resources/imgs/hiragana_a.png")
    position_2_label.configure(image=position_2_image)
    position_2_label.image = position_2_image

    entry = tk.Entry(root, width=8, justify='center', font='Arial 24', borderwidth=0, textvariable=answer)
    entry.focus()
    entry.grid(column=0, row=0, pady=(200,0), padx=(40,0))
    entry.bind('<Return>', check_answer)

    next_btn_image = tk.PhotoImage(file="resources/imgs/button_next.png")
    next_btn = tk.Button(root, command=lambda: print(), border=0, borderwidth=0, background="#bdd1ff", activebackground="#bdd1ff")
    next_btn.config(image=next_btn_image)
    next_btn_image.image = next_btn_image
    next_btn.grid(column=0, row=1, pady=(0, 30), padx=(20,0))

    count_label = tk.Label(borderwidth=5, highlightthickness=0, background="#bdd1ff", text="CORRECT: 0/92 (0%)", font='Arial 24')
    count_label.grid(column=1, row=3)

    answer_label = tk.Label(borderwidth=5, highlightthickness=0, background="#bdd1ff", text="ANSWER", font='Arial 24')
    answer_label.grid(column=2, row=1)

    exit_btn_image = tk.PhotoImage(file="resources/imgs/button_exit.png")
    exit_btn = tk.Button(root, command=lambda: change_page(root, 'main_menu'), border=0, borderwidth=0, background="#bdd1ff", activebackground="#bdd1ff")
    exit_btn.config(image=exit_btn_image)
    exit_btn_image.image = exit_btn_image
    exit_btn.grid(column=1, row=4, pady=(0, 30))





def change_page(root, target):
    mixer.music.stop()
    for widgets in root.winfo_children():
        widgets.destroy()
    if target == 'learn_menu':
        learn_menu(root)
    elif target == 'kana_selection':
        kana_selection_menu(root)
    elif target == 'main_menu':
        main_menu(root)
    elif target == 'practice':
        practice(root)


def increase_page_count():
    global current_page_number
    current_page_number += 1
    change_page(root, 'learn_menu')


def decrease_page_count():
    global current_page_number
    current_page_number -= 1
    change_page(root, 'learn_menu')


def set_learning_mode(kana):
    global selected_kana
    if kana == 'hiragana':
        selected_kana = 'hiragana'
    elif kana == 'katakana':
        selected_kana = 'katakana'
    change_page(root, 'learn_menu')


def key_pressed(event):
    global current_page
    #print(event.keysym)
    if event.keysym == 'Right' and current_page == 'learn_menu' and current_page_number < 9:
        increase_page_count()
    elif event.keysym == 'Left' and current_page == 'learn_menu' and current_page_number > 0:
        decrease_page_count()
    elif event.keysym == 'Escape' and current_page == 'learn_menu':
        change_page(root, 'main_menu')


def play_sound(file):
    if file == 'aiueo':
        mixer.music.load('resources/sounds/aiueo.mp3')
    elif file == 'kakikukeko':
        mixer.music.load('resources/sounds/kakikukeko.mp3')
    elif file == 'sashisuseso':
        mixer.music.load('resources/sounds/sashisuseso.mp3')
    elif file == 'tachitsuteto':
        mixer.music.load('resources/sounds/tachitsuteto.mp3')
    elif file == 'naninuneno':
        mixer.music.load('resources/sounds/naninuneno.mp3')
    elif file == 'hahifuheho':
        mixer.music.load('resources/sounds/hahifuheho.mp3')
    elif file == 'mamimumemo':
        mixer.music.load('resources/sounds/mamimumemo.mp3')
    elif file == 'yayuyo':
        mixer.music.load('resources/sounds/yayuyo.mp3')
    elif file == 'rarirurero':
        mixer.music.load('resources/sounds/rarirurero.mp3')
    elif file == 'waon':
        mixer.music.load('resources/sounds/waon.mp3')

    mixer.music.play()


root = tk.Tk()
root.title("DOGAKU")
root.iconbitmap("resources/imgs/dokagu_icon.ico")
root.resizable(False, False)
root.configure(bg="#bdd1ff", borderwidth=0)
root.bind("<Key>", key_pressed)
root.eval('tk::PlaceWindow . center')

main_menu(root)
root.mainloop()

